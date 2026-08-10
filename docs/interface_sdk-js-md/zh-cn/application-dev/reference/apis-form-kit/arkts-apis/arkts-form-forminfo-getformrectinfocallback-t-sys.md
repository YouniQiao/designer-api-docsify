# GetFormRectInfoCallback（系统接口）

```TypeScript
type GetFormRectInfoCallback = (formId: string) => Promise<formInfo.Rect>
```

Get form rect info callback

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-formInfo-type GetFormRectInfoCallback = (formId: string) => Promise<formInfo.Rect>--><!--Device-formInfo-type GetFormRectInfoCallback = (formId: string) => Promise<formInfo.Rect>-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| formId | string | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;formInfo.Rect&gt; | form rect info |

