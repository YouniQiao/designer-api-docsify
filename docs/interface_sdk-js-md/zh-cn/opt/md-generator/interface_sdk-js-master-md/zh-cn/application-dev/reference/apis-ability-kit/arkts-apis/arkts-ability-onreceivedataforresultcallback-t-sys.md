# OnReceiveDataForResultCallback（系统接口）

```TypeScript
export type OnReceiveDataForResultCallback = (data: Record<string, RecordData>) => Record<string, RecordData>
```

从UIExtensionComponent控件接收数据带返回值的回调方法。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export type OnReceiveDataForResultCallback = (data: Record<string, RecordData>) => Record<string, RecordData>--><!--Device-unnamed-export type OnReceiveDataForResultCallback = (data: Record<string, RecordData>) => Record<string, RecordData>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | Record&lt;string, [RecordData](../../apis-arkdata/arkts-apis/arkts-arkdata-preferences-recorddata-t.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Record&lt;string, [RecordData](../../apis-arkdata/arkts-apis/arkts-arkdata-preferences-recorddata-t.md)&gt; |
