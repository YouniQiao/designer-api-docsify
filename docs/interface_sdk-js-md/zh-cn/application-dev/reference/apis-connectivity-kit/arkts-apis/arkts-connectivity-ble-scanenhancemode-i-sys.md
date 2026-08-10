# ScanEnhanceMode（系统接口）

Describes the configuration of scan enhance mode.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

<!--Device-ble-interface ScanEnhanceMode--><!--Device-ble-interface ScanEnhanceMode-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { ble } from 'kits/@kit.ConnectivityKit';
```

## enhanceMode

```TypeScript
enhanceMode: EnhanceMode
```

The mode of scan enhance.

**类型：** [EnhanceMode](arkts-connectivity-ble-enhancemode-e-sys.md)

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ScanEnhanceMode-enhanceMode: EnhanceMode--><!--Device-ScanEnhanceMode-enhanceMode: EnhanceMode-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**系统接口：** 此接口为系统接口。

## timeout

```TypeScript
timeout: int
```

The duration of scan enhance.The value range is all integers.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ScanEnhanceMode-timeout: int--><!--Device-ScanEnhanceMode-timeout: int-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**系统接口：** 此接口为系统接口。

