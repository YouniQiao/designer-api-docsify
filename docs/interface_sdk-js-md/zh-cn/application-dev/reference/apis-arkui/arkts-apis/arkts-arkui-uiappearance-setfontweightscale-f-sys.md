# setFontWeightScale（系统接口）

## 导入模块

```TypeScript
import { uiAppearance } from 'kits/@kit.ArkUI';
```

## setFontWeightScale

```TypeScript
function setFontWeightScale(fontWeightScale: number): Promise<void>
```

设置系统字体粗细。

**起始版本：** 12

**需要权限：** ohos.permission.UPDATE_CONFIGURATION

**系统能力：** SystemCapability.ArkUI.UiAppearance

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [fontWeightScale](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-configuration-configuration-i.md) | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [500001](../errorcode-uiappearance.md#500001-内部错误) |
