import voluptuous as vol
from solax.inverter import InverterPost
from solax.units import Units, Total
from solax.utils import startswith


class X3(InverterPost):
    _schema = vol.Schema(
        {
            vol.Required("type"): vol.All(str, startswith("X3-")),
            vol.Required("SN"): str,
            vol.Required("ver"): str,
            vol.Required("Data"): vol.Schema(
                vol.All(
                    [vol.Coerce(float)],
                    vol.Any(vol.Length(min=102, max=103), vol.Length(min=107, max=107)),
                )
            ),
            vol.Required("Information"): vol.Schema(vol.All(vol.Length(min=9, max=9))),
        },
        extra=vol.REMOVE_EXTRA,
    )

    # pylint: disable=duplicate-code
    @classmethod
    def response_decoder(cls):
        return {
            "PV1 Current": (0, Units.A),
            "PV2 Current": (1, Units.A),
            "PV1 Voltage": (2, Units.V),
            "PV2 Voltage": (3, Units.V),
            "Output Current Phase 1": (4, Units.A),
            "Network Voltage Phase 1": (5, Units.V),
            "AC Power": (6, Units.W),
            "Inverter Temperature": (7, Units.C),
            "Today's Energy": (8, Units.KWH),
            "Total Energy": (9, Total(Units.KWH)),
            "Exported Power": (10, Units.W),
            "PV1 Power": (11, Units.W),
            "PV2 Power": (12, Units.W),
            "Battery Voltage": (13, Units.V),
            "Battery Current": (14, Units.A),
            "Battery Power": (15, Units.W),
            "Battery Temperature": (16, Units.C),
            "Battery Remaining Capacity": (21, Units.PERCENT),
            "Total Feed-in Energy": (41, Total(Units.KWH)),
            "Total Consumption": (42, Total(Units.KWH)),
            "Power Now Phase 1": (43, Units.W),
            "Power Now Phase 2": (44, Units.W),
            "Power Now Phase 3": (45, Units.W),
            "Output Current Phase 2": (46, Units.A),
            "Output Current Phase 3": (47, Units.A),
            "Network Voltage Phase 2": (48, Units.V),
            "Network Voltage Phase 3": (49, Units.V),
            "Grid Frequency Phase 1": (50, Units.HZ),
            "Grid Frequency Phase 2": (51, Units.HZ),
            "Grid Frequency Phase 3": (52, Units.HZ),
            "EPS Voltage": (53, Units.V),
            "EPS Current": (54, Units.A),
            "EPS Power": (55, Units.W),
            "EPS Frequency": (56, Units.HZ),
        }
