# GetLiveFormStatusCallback（系统接口）

```TypeScript
type GetLiveFormStatusCallback = () => Record<string, string>
```

获取互动卡片状态的回调。

**起始版本：** 20

<!--Device-formInfo-type GetLiveFormStatusCallback = () => Record<string, string>--><!--Device-formInfo-type GetLiveFormStatusCallback = () => Record<string, string>-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Record&lt;string, string&gt; | 返回卡片的状态信息。key为formID，value为卡片的状态信息。状态信息有"INACTIVE"、"PAUSE"、"ACTIVE"。 |
