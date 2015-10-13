import fedmsg.consumers

class EpelRebuild(fedmsg.consumers.FedmsgConsumer):
    topic = 'org.fedoraproject.prod.git.*'
    config_key = 'epelrebuild'

    def __init__(self, *args, **kwargs):
        super(EpelRebuild, self).__init__(*args, **kwargs)

    def consume(self, msg):
        branches = ['el5', 'el6', 'epel7']

        msg = msg.get('body', {})
        print msg

        #if msg['branch'] in branches:
        #    print "WOULD REBUILD: {0}".format(msg['msg']['repo'])

    def process(self, msg):
        pass
