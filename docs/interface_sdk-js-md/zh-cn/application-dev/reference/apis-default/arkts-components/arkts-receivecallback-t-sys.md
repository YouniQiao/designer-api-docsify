# ReceiveCallback（系统接口）

```TypeScript
export type ReceiveCallback = Callback<Record<string, RecordData>>
```

回调函数，用于封装被拉起的Ability发送的数据。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export type ReceiveCallback = Callback<Record<string, RecordData>>--><!--Device-unnamed-export type ReceiveCallback = Callback<Record<string, RecordData>>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**属性类型：** [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[Record](../../apis-arkts/arkts-apis/arkts-arkts-map-record-c.md)&lt;string, [RecordData](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-recorddata-t.md)&gt;&gt;

