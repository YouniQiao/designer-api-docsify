# UpgradeTaskCallback（系统接口）

```TypeScript
export type UpgradeTaskCallback = (eventInfo: EventInfo) => void
```

事件回调。  
**版本说明**： 从API version 23开始支持。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Update.UpdateService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| eventInfo | [EventInfo](arkts-basicservices-update-eventinfo-i-sys.md) | 是 |
