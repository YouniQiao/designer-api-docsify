# GetFormRectInfoCallback（系统接口）

```TypeScript
type GetFormRectInfoCallback = (formId: string) => Promise<formInfo.Rect>
```

卡片位置、尺寸查询回调。使用Promise异步回调。

**起始版本：** 20

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| formId | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[formInfo.Rect](arkts-form-forminfo-rect-i.md)&gt; |
