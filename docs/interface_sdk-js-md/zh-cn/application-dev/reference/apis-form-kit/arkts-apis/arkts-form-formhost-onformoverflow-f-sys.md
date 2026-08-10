# onFormOverflow（系统接口）

## 导入模块

```TypeScript
import { formHost } from 'kits/@kit.FormKit';
```

## onFormOverflow

```TypeScript
function onFormOverflow(callback: Callback<formInfo.OverflowRequest>): void
```

Listens to the event of formOverflow.

You can use this method to listen to the event of formOverflow.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-formHost-function onFormOverflow(callback: Callback<formInfo.OverflowRequest>): void--><!--Device-formHost-function onFormOverflow(callback: Callback<formInfo.OverflowRequest>): void-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;formInfo.OverflowRequest&gt; | 是 | The callback of formOverflow. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 202 | The application is not a system application. |

