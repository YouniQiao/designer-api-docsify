# WifiProfile

Represents the Wi-Fi configuration information.

**Since:** 12

<!--Device-wifiManager-interface WifiProfile--><!--Device-wifiManager-interface WifiProfile-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## Modules to Import

```TypeScript
import { wifiManager } from '@kit.MDMKit';
```

## bssid

```TypeScript
bssid?: string
```

MAC address of the Wi-Fi hotspot. To obtain the MAC address, enable **Enable Wi-Fi verbose logging** under **Settings** > **System & updates** > **Developer options** first, and then go to the WLAN list to check the MAC address. If a Wi-Fi network has multiple MAC addresses, all of them must be added here.

**Type:** string

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

<!--Device-WifiProfile-bssid?: string--><!--Device-WifiProfile-bssid?: string-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## creatorUid

```TypeScript
creatorUid?: number
```

ID of the creator.

**Type:** number

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

<!--Device-WifiProfile-creatorUid?: number--><!--Device-WifiProfile-creatorUid?: number-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## disableReason

```TypeScript
disableReason?: number
```

Reason for disabling Wi-Fi.

**Type:** number

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

<!--Device-WifiProfile-disableReason?: number--><!--Device-WifiProfile-disableReason?: number-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## eapProfile

```TypeScript
eapProfile?: WifiEapProfile
```

Extensible Authentication Protocol (EAP) configuration. This field is mandatory only when **securityType** is set to **WIFI_SEC_TYPE_EAP**.

**Type:** WifiEapProfile

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

<!--Device-WifiProfile-eapProfile?: WifiEapProfile--><!--Device-WifiProfile-eapProfile?: WifiEapProfile-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## ipType

```TypeScript
ipType?: IpType
```

IP address type.

**Type:** IpType

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

<!--Device-WifiProfile-ipType?: IpType--><!--Device-WifiProfile-ipType?: IpType-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## isHiddenSsid

```TypeScript
isHiddenSsid?: boolean
```

Whether the network is hidden. The value **true** indicates that the network is hidden; the value **false** indicates the opposite.

**Type:** boolean

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

<!--Device-WifiProfile-isHiddenSsid?: boolean--><!--Device-WifiProfile-isHiddenSsid?: boolean-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## netId

```TypeScript
netId?: number
```

Network ID allocated.

**Type:** number

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

<!--Device-WifiProfile-netId?: number--><!--Device-WifiProfile-netId?: number-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## preSharedKey

```TypeScript
preSharedKey: string
```

Pre-shared key.

**Type:** string

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

<!--Device-WifiProfile-preSharedKey: string--><!--Device-WifiProfile-preSharedKey: string-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## randomMacAddr

```TypeScript
randomMacAddr?: string
```

MAC address. This field is mandatory when **randomMacType** is set to device MAC address.

**Type:** string

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

<!--Device-WifiProfile-randomMacAddr?: string--><!--Device-WifiProfile-randomMacAddr?: string-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## randomMacType

```TypeScript
randomMacType?: number
```

Random MAC. The value **0** indicates a random MAC address, and the value **1** indicates device MAC address.

**Type:** number

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

<!--Device-WifiProfile-randomMacType?: number--><!--Device-WifiProfile-randomMacType?: number-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## securityType

```TypeScript
securityType: WifiSecurityType
```

Security type.

**Type:** WifiSecurityType

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

<!--Device-WifiProfile-securityType: WifiSecurityType--><!--Device-WifiProfile-securityType: WifiSecurityType-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## ssid

```TypeScript
ssid: string
```

Name of the Wi-Fi hotspot, in UTF-8 format.

**Type:** string

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

<!--Device-WifiProfile-ssid: string--><!--Device-WifiProfile-ssid: string-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## staticIp

```TypeScript
staticIp?: IpProfile
```

Static IP address information. This field is mandatory when **ipType** is set to **STATIC**.

**Type:** IpProfile

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

<!--Device-WifiProfile-staticIp?: IpProfile--><!--Device-WifiProfile-staticIp?: IpProfile-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

