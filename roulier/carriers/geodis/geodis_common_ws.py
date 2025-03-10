"""Store infos about ws"""
from .geodis_api_ws import GeodisApiWs
from .geodis_api_rest_ws import (
    GeodisApiTracking,
    GeodisApiTrackingList,
)
from .geodis_api_find_localite_ws import GeodisApiFindLocaliteWs


GEODIS_INFOS = {
    "demandeImpressionEtiquette": {
        "xmlns": "http://impression.service.web.etiquette.geodis.com",
        "endpoint": "http://espace.geodis.com/geolabel/services/ImpressionEtiquette",  # nopep8
        "endpoint_test": "http://espace.recette.geodis.com/geolabel/services/ImpressionEtiquette",  # nopep8
        "api": GeodisApiWs,
    },
    "findLocalite": {
        "xmlns": "http://localite.service.web.etiquette.geodis.com",
        "endpoint": "http://espace.geodis.com/geolabel/services/RechercherLocalite",  # nopep8
        "endpoint_test": "http://espace.recette.geodis.com/geolabel/services/RechercherLocalite",  # nopep8
        "api": GeodisApiFindLocaliteWs,
    },
    "trackingList": {
        "endpoint": "https://espace-client.geodis.com/services",
        "service": "api/zoomclient/recherche-envois",
        "api": GeodisApiTrackingList,
    },
    "tracking": {
        "endpoint": "https://espace-client.geodis.com/services",
        "service": "api/zoomclient/recherche-envoi",
        "api": GeodisApiTracking,
    },
}
