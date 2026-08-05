# WifiAccessInfo

Represents Wi-Fi access information containing Service Set Identifier (SSID) and Basic Service Set Identifier ( BSSID).

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

<!--Device-wifiManager-interface WifiAccessInfo--><!--Device-wifiManager-interface WifiAccessInfo-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## bssid

```TypeScript
bssid?: string
```

MAC address of the Wi-Fi hotspot, for example, **00:11:22:33:44:55**. To obtain the MAC address, enable **Enable Wi-Fi verbose logging** under **Settings** > **System & updates** > **Developer options** first, and then go to the WLAN list to check the MAC address. If a Wi-Fi network has multiple MAC addresses, all of them must be added here. This property is optional when the [addDisallowedWifiList]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ and [removeDisallowedWifiList]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ APIs are called. The default value is an empty string. This property is optional (available since API version 21) when the [addAllowedWifiList]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ and [removeAllowedWifiList]\_\_\_JSDOC\_LINK\_DESC\_USD\_3\_\_\_ APIs are called. The default value is an empty string. However, this property is mandatory in API version 20 and earlier versions.

**Type:** string

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WifiAccessInfo-bssid?: string--><!--Device-WifiAccessInfo-bssid?: string-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## ssid

```TypeScript
ssid: string
```

Name of the Wi-Fi hotspot. The encoding format is UTF-8 and the maximum length is 32 bytes (three bytes for each Chinese character and one byte for each English character).

**Type:** string

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WifiAccessInfo-ssid: string--><!--Device-WifiAccessInfo-ssid: string-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

