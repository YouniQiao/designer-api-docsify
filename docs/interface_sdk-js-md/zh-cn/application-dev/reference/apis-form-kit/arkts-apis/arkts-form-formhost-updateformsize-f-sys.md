# updateFormSize（系统接口）

## 导入模块

```TypeScript
import { formHost } from 'kits/@kit.FormKit';
```

## updateFormSize

```TypeScript
function updateFormSize(formId: string, newDimension: formInfo.FormDimension, newRect: formInfo.Rect): void
```

调整卡片尺寸。

**起始版本：** 20

**需要权限：** ohos.permission.REQUIRE_FORM

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| formId | string | 是 |
| newDimension | formInfo.FormDimension | 是 |
| newRect | formInfo.Rect | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [16501000](../errorcode-form.md#16501000-内部功能错误) |
| [16501001](../errorcode-form.md#16501001-卡片id不存在) |
| [16501012](../errorcode-form.md#16501012-卡片尺寸错误) |
