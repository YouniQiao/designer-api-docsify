# QueryCustomContentEvent

```TypeScript
type QueryCustomContentEvent = (queryType: CustomType[]) => Promise<CustomElement>
```

自定义内容查询事件。使用Promise异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-avMusicTemplate-type QueryCustomContentEvent = (queryType: CustomType[]) => Promise<CustomElement>--><!--Device-avMusicTemplate-type QueryCustomContentEvent = (queryType: CustomType[]) => Promise<CustomElement>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| queryType | [CustomType](arkts-avsession-avmusictemplate-customtype-t.md)[] | Yes | 自定义类型：包含用户基本信息、界面选项卡配置、代码编译选项和系统设置项。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;CustomElement&gt; | Promise对象，返回我的页面的自定义元素。 |

