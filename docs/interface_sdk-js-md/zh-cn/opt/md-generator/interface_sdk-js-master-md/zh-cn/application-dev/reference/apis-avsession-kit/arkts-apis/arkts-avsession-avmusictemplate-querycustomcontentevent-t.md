# QueryCustomContentEvent

```TypeScript
type QueryCustomContentEvent = (queryType: CustomType[]) => Promise<CustomElement>
```

自定义内容查询事件。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-avMusicTemplate-type QueryCustomContentEvent = (queryType: CustomType[]) => Promise<CustomElement>--><!--Device-avMusicTemplate-type QueryCustomContentEvent = (queryType: CustomType[]) => Promise<CustomElement>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [queryType](../../apis-ability-kit/arkts-apis/arkts-ability-insightintent-queryentityparam-i.md) | [CustomType](arkts-avsession-avmusictemplate-customtype-t.md)[] | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[CustomElement](arkts-avsession-avmusictemplate-customelement-i.md)&gt; |
