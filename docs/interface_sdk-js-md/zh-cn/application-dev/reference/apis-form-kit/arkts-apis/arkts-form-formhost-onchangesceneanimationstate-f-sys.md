# onChangeSceneAnimationState（系统接口）

## 导入模块

```TypeScript
import { formHost } from '@kit.FormKit';
```

## onChangeSceneAnimationState

```TypeScript
function onChangeSceneAnimationState(callback: Callback<formInfo.ChangeSceneAnimationStateRequest>): void
```

Listens to the event of change scene animation state.You can use this method to listen to the event of change scene animation state.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;formInfo.ChangeSceneAnimationStateRequest&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

**示例**

```TypeScript
'use static'

import { formHost, formInfo } from '@kit.FormKit';
import { BusinessError } from '@kit.BasicServicesKit';

let callback = (data: formInfo.ChangeSceneAnimationStateRequest) => {
  console.info( 'testTag', `onChangeSceneAnimationState ChangeSceneAnimationStateRequest, data.formId: ${data.formId}`);
}
try {
  formHost.onChangeSceneAnimationState(callback);
  console.info( 'testTag EntryFormAbility', 'onChangeSceneAnimationState on success');
} catch (error) {
  console.info( 'testTag EntryFormAbility', `onChangeSceneAnimationState on catch error ${error.code}, ${error.message}`);
}
```
