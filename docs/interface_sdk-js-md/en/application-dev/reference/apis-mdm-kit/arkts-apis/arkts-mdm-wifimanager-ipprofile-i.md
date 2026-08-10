# IpProfile

IP配置信息。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-wifiManager-interface IpProfile--><!--Device-wifiManager-interface IpProfile-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## Modules to Import

```TypeScript
import { wifiManager } from 'kits/@kit.MDMKit';
```

## dnsServers

```TypeScript
dnsServers: number[]
```

DNS服务器，数组内最多包含首选DNS服务器和备用DNS服务器两个地址。地址值范围0.0.0.0到255.255.255.255。

**Type:** number[]

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IpProfile-dnsServers: number[]--><!--Device-IpProfile-dnsServers: number[]-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## domains

```TypeScript
domains: Array<string>
```

域信息。

**Type:** Array&lt;string&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IpProfile-domains: Array<string>--><!--Device-IpProfile-domains: Array<string>-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## gateway

```TypeScript
gateway: number
```

默认网关，十进制表示，通常是路由器的IP地址。地址值范围0.0.0.0到255.255.255.255。

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IpProfile-gateway: number--><!--Device-IpProfile-gateway: number-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## ipAddress

```TypeScript
ipAddress: number
```

IP地址，十进制表示，正常点分十进制写法为192.168.1.1，对应的十进制为3232235777。地址值范围0.0.0.0到255.255.255.255。

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IpProfile-ipAddress: number--><!--Device-IpProfile-ipAddress: number-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## prefixLength

```TypeScript
prefixLength: number
```

子网掩码。地址值范围0.0.0.0到255.255.255.255。

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IpProfile-prefixLength: number--><!--Device-IpProfile-prefixLength: number-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

