import json

class Sample:
    def sample_data():
        data = {
            "links": {
                "self": "http://www.neowsapp.com/rest/v1/neo/2000433?api_key=DEMO_KEY"
            },
            "id": "2000433",
            "neo_reference_id": "2000433",
            "name": "433 Eros (A898 PA)",
            "name_limited": "Eros",
            "designation": "433",
            "nasa_jpl_url": "http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=2000433",
            "absolute_magnitude_h": 10.4,
            "estimated_diameter": {
                "kilometers": {
                    "estimated_diameter_min": 22.1082810359,
                    "estimated_diameter_max": 49.435619262
                },
                "meters": {
                    "estimated_diameter_min": 22108.281035909,
                    "estimated_diameter_max": 49435.619261962
                },
                "miles": {
                    "estimated_diameter_min": 13.7374446956,
                    "estimated_diameter_max": 30.7178601764
                },
                "feet": {
                    "estimated_diameter_min": 72533.7327538517,
                    "estimated_diameter_max": 162190.3570994153
                }
            },
            "is_potentially_hazardous_asteroid": false,
            "close_approach_data": [
                {
                    "close_approach_date": "1900-12-27",
                    "close_approach_date_full": "1900-Dec-27 01:30",
                    "epoch_date_close_approach": -2177879400000,
                    "relative_velocity": {
                        "kilometers_per_second": "5.5786203614",
                        "kilometers_per_hour": "20083.0333009607",
                        "miles_per_hour": "12478.8158863664"
                    },
                    "miss_distance": {
                        "astronomical": "0.3149291092",
                        "lunar": "122.5074234788",
                        "kilometers": "47112723.937317404",
                        "miles": "29274489.1785480152"
                    },
                    "orbiting_body": "Earth"
                }
            ],
            "orbital_data": {
                "orbit_id": "658",
                "orbit_determination_date": "2020-09-06 18:22:27",
                "first_observation_date": "1893-10-29",
                "last_observation_date": "2020-09-03",
                "data_arc_in_days": 46330,
                "observations_used": 8767,
                "orbit_uncertainty": "0",
                "minimum_orbit_intersection": ".148623",
                "jupiter_tisserand_invariant": "4.582",
                "epoch_osculation": "2459000.5",
                "eccentricity": ".2229512647434284",
                "semi_major_axis": "1.458045729081037",
                "inclination": "10.83054121829922",
                "ascending_node_longitude": "304.2993259000444",
                "orbital_period": "643.0654021001488",
                "perihelion_distance": "1.132972589728666",
                "perihelion_argument": "178.8822959227224",
                "aphelion_distance": "1.783118868433408",
                "perihelion_time": "2459159.351922368362",
                "mean_anomaly": "271.0717325705167",
                "mean_motion": ".5598186418120109",
                "equinox": "J2000",
                "orbit_class": {
                    "orbit_class_type": "AMO",
                    "orbit_class_description": "Near-Earth asteroid orbits similar to that of 1221 Amor",
                    "orbit_class_range": "1.017 AU < q (perihelion) < 1.3 AU"
                },
                "is_sentry_object": false
            }
        }