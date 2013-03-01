__all__ = ['app', ]
import flask

from flask_debugtoolbar import DebugToolbarExtension

app = flask.Flask(__name__)
app.config.from_object(__name__)
app.config['MONGODB_SETTINGS'] = {'DB': 'testing'}
app.config['TESTING'] = True
app.config['SECRET_KEY'] = 'flask+mongoengine=<3'
app.debug = True
app.config['DEBUG_TB_PANELS'] = (
             'flask.ext.debugtoolbar.panels.versions.VersionDebugPanel',
             'flask.ext.debugtoolbar.panels.timer.TimerDebugPanel',
             'flask.ext.debugtoolbar.panels.headers.HeaderDebugPanel',
             'flask.ext.debugtoolbar.panels.request_vars.RequestVarsDebugPanel',
             'flask.ext.debugtoolbar.panels.template.TemplateDebugPanel',
             'flask.ext.debugtoolbar.panels.logger.LoggingPanel',
             'flask.ext.mongoengine.panels.MongoDebugPanel'
             )

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


DebugToolbarExtension(app)

