from schema import Schema, And, Use
from engine.helpers.const.service_characteristics import TYPE, REGIONS, DEPLOYMENT_TIME, LEASING_PERIOD, CURRENCIES

recommend_provider_schema = Schema({'region': [And(str, Use(str.upper), lambda s: s in REGIONS)],
                  'serviceType':  {'value': [And(str, Use(str.upper), lambda s: s in TYPE)],
                                   'weight': And(Use(int), lambda n: 0 <= n <= 2)},
                  'deploymentTime':  {'value': And(str, Use(str.upper), lambda s: s in DEPLOYMENT_TIME),
                                      'weight': And(Use(int), lambda n: 0 <= n <= 2)},
                  'leasingPeriod':  {'value': And(str, Use(str.upper), lambda s: s in LEASING_PERIOD),
                                     'weight': And(Use(int), lambda n: 0 <= n <= 2)},
                  'budget':  {'currency': And(str, Use(str.upper), lambda s: s in CURRENCIES),
                              'maxPrice': And(Use(int)),
                              'weight': And(Use(int), lambda n: 0 <= n <= 2)}})