import logging
from bika.lims import api
from bika.lims.browser import BrowserView
from bika.lims.interfaces import IFrontPageAdapter
from plone import api as ploneapi
from plone.protect.utils import addTokenToUrl
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.component import getAdapters
from Products.CMFCore.utils import getToolByName
from Products.PluggableAuthService.interfaces.plugins import IChallengePlugin
def FrontPageView(self):
        self.icon = "{}/{}".format(
            self.portal_url, "/++resource++bika.lims.images/chevron_big.png")
        setup = api.get_setup()
        login_url = "{}/{}".format(self.portal_url, "login")
        landingpage = setup.getLandingPage()

        # Anonymous Users get either redirected to the std. bika-frontpage or
        # to the custom landing page, which is set in setup. If no landing
        # page setup, then redirect to login page.
        if self.is_anonymous_user():
            # Redirect to the selected Landing Page(
            if landingpage:
                return self.request.response.redirect(
                    landingpage.absolute_url())
            # Use first available challenge plugin
            pas = getToolByName(self.portal, "acl_users") 
            plugin_id = next(iter(pas.plugins.listPluginIds(IChallengePlugin)), None)
            if(plugin_id):
                plugin = pas[plugin_id]
                plugin.challenge(self.request, self.request.response)
            else:
                # Redirect to login page
                return self.request.response.redirect(login_url)

            
            
        # Authenticated Users get either the Dashboard, the std. login page
        # or the custom landing page. Furthermore, they can switch between the
        # Dashboard and the landing page.
        # Add-ons can have an adapter for front-page-url as well.
        for name, adapter in getAdapters((self.context,), IFrontPageAdapter):
            redirect_to = adapter.get_front_page_url()
            if redirect_to:
                return self.request.response.redirect(
                    self.portal_url + redirect_to)

        # First precedence: Request parameter `redirect_to`
        redirect_to = self.request.form.get("redirect_to", None)
        if redirect_to == "dashboard":
            return self.request.response.redirect(
                self.portal_url + "/senaite-dashboard")
        if redirect_to == "frontpage":
            if landingpage:
                return self.request.response.redirect(
                    landingpage.absolute_url())
            return self.template()

        # Second precedence: Dashboard enabled
        if self.is_dashboard_enabled():
            roles = self.get_user_roles()
            allowed = ["Manager", "LabManager", "LabClerk"]
            if set(roles).intersection(allowed):
                url = addTokenToUrl("{}/{}".format(
                    self.portal_url, "senaite-dashboard"))
                return self.request.response.redirect(url)
            if "Sampler" in roles or "SampleCoordinator" in roles:
                url = addTokenToUrl("{}/{}".format(
                    self.portal_url,
                    "samples?samples_review_state=to_be_sampled"))
                return self.request.response.redirect(url)

        # Third precedence: Custom Landing Page
        if landingpage:
            return self.request.response.redirect(landingpage.absolute_url())

        # Last precedence: Front Page
        return self.template()