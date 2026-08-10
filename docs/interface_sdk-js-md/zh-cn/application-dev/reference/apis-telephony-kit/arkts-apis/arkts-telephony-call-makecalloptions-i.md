# MakeCallOptions

Indicates the options of make call.

**起始版本：** 24

**ArkTS模式：** ArkTS-Dyn起始版本为24；ArkTS-Sta起始版本为26.0.0。

<!--Device-call-export interface MakeCallOptions--><!--Device-call-export interface MakeCallOptions-End-->

**系统能力：** SystemCapability.Applications.Contacts

## 导入模块

```TypeScript
import { call } from 'kits/@kit.TelephonyKit';
```

## isCustomAccessibility

```TypeScript
isCustomAccessibility?: boolean
```

Whether the third-party app supports custom accessibility features.Default value: false.

**类型：** boolean

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-MakeCallOptions-isCustomAccessibility?: boolean--><!--Device-MakeCallOptions-isCustomAccessibility?: boolean-End-->

**系统能力：** SystemCapability.Applications.Contacts

## isHideDialScreen

```TypeScript
isHideDialScreen?: boolean
```

Whether to hide the dialer screen after call ends.&lt;br&gt;Default value: false.

**类型：** boolean

**起始版本：** 24

**ArkTS模式：** ArkTS-Dyn起始版本为24；ArkTS-Sta起始版本为26.0.0。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

<!--Device-MakeCallOptions-isHideDialScreen?: boolean--><!--Device-MakeCallOptions-isHideDialScreen?: boolean-End-->

**系统能力：** SystemCapability.Applications.Contacts

