import os
import logging

def zap_access_target(zap, target):
    res = zap.exim.import_urls('/zap/wrk/url.txt')
    logging.debug('Import warnings: ' + str(res))
