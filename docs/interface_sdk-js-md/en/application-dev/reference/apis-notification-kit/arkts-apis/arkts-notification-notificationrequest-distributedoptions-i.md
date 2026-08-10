# DistributedOptions

描述跨设备协同选项。预留能力，暂未支持。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface DistributedOptions--><!--Device-unnamed-export interface DistributedOptions-End-->

**System capability:** SystemCapability.Notification.Notification

## isDistributed

```TypeScript
isDistributed?: boolean
```

是否支持跨设备协同通知。默认为true。

- true：支持跨设备协同通知。  
- false：不支持跨设备协同通知。

**Type:** boolean

**Default:** true

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-DistributedOptions-isDistributed?: boolean--><!--Device-DistributedOptions-isDistributed?: boolean-End-->

**System capability:** SystemCapability.Notification.Notification

## supportDisplayDevices

```TypeScript
supportDisplayDevices?: Array<string>
```

可以同步通知到的设备列表。

**Type:** Array&lt;string&gt;

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-DistributedOptions-supportDisplayDevices?: Array<string>--><!--Device-DistributedOptions-supportDisplayDevices?: Array<string>-End-->

**System capability:** SystemCapability.Notification.Notification

## supportOperateDevices

```TypeScript
supportOperateDevices?: Array<string>
```

可以打开通知的设备列表。

**Type:** Array&lt;string&gt;

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-DistributedOptions-supportOperateDevices?: Array<string>--><!--Device-DistributedOptions-supportOperateDevices?: Array<string>-End-->

**System capability:** SystemCapability.Notification.Notification

