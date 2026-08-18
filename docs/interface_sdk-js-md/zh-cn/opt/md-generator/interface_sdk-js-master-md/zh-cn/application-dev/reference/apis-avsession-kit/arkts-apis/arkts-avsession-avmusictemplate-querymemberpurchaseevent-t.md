# QueryMemberPurchaseEvent

```TypeScript
type QueryMemberPurchaseEvent = (memberPurchaseType: MemberPurchaseType) => Promise<MemberPurchaseInfo[]>
```

购买会员查询事件。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-avMusicTemplate-type QueryMemberPurchaseEvent = (memberPurchaseType: MemberPurchaseType) => Promise<MemberPurchaseInfo[]>--><!--Device-avMusicTemplate-type QueryMemberPurchaseEvent = (memberPurchaseType: MemberPurchaseType) => Promise<MemberPurchaseInfo[]>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [memberPurchaseType](arkts-avsession-avmusictemplate-memberpurchaseinfo-i.md) | [MemberPurchaseType](arkts-avsession-avmusictemplate-memberpurchasetype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[MemberPurchaseInfo](arkts-avsession-avmusictemplate-memberpurchaseinfo-i.md)[]&gt; |
