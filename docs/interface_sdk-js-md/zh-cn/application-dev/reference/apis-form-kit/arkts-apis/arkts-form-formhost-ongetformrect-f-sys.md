# onGetFormRect（系统接口）

## 导入模块

```TypeScript
import { formHost } from 'kits/@kit.FormKit';
```

## onGetFormRect

```TypeScript
function onGetFormRect(callback: formInfo.GetFormRectInfoCallback): void
```

Listens to the event of get form rect.

You can use this method to listen to the event of get form rect.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-formHost-function onGetFormRect(callback: formInfo.GetFormRectInfoCallback): void--><!--Device-formHost-function onGetFormRect(callback: formInfo.GetFormRectInfoCallback): void-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | formInfo.GetFormRectInfoCallback | 是 | The callback of get form rect. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 202 | The application is not a system application. |

