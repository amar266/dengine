from pecan import make_app, conf
from pecan.hooks import TransactionHook
from deployerengine import model


def setup_app(config):

    model.init_model()
    app_conf = dict(config.app)

    return make_app(
        app_conf.pop('root'),
        logging=getattr(config, 'logging', {}),
        **app_conf
    )

app = make_app(
    conf.app.root,
    static_root     = conf.app.static_root,
    template_path   = conf.app.template_path,
    debug           = conf.app.debug,
    hooks           = [
        TransactionHook(
            model.start,
            model.start_read_only,
            model.commit,
            model.rollback,
            model.clear
        )
    ]
)
