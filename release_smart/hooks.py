# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "release_smart"
app_title = "Release"
app_publisher = "revant"
app_description = "release"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "revant.one@gmail.com"
app_version = "0.0.9"
app_license = "GPL v3"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/release_smart/css/release_smart.css"
# app_include_js = "/assets/release_smart/js/release_smart.js"

# include js, css files in header of web template
# web_include_css = "/assets/release_smart/css/release_smart.css"
# web_include_js = "/assets/release_smart/js/release_smart.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "release_smart.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "release_smart.install.before_install"
# after_install = "release_smart.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "release_smart.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"release_smart.tasks.all"
# 	],
# 	"daily": [
# 		"release_smart.tasks.daily"
# 	],
# 	"hourly": [
# 		"release_smart.tasks.hourly"
# 	],
# 	"weekly": [
# 		"release_smart.tasks.weekly"
# 	]
# 	"monthly": [
# 		"release_smart.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "release_smart.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "release_smart.event.get_events"
# }

