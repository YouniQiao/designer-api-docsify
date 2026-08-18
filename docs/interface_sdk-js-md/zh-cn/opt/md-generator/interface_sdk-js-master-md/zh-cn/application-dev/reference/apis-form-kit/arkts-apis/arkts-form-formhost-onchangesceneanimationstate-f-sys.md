# onChangeSceneAnimationState（系统接口）

## 导入模块

```TypeScript
```

## onChangeSceneAnimationState

```TypeScript
function onChangeSceneAnimationState(callback: Callback<formInfo.ChangeSceneAnimationStateRequest>): void
```

Listens to the event of change scene animation state. You can use this method to listen to the event of change scene animation state.

**起始版本：** 23

<!--Device-formHost-function onChangeSceneAnimationState(callback: Callback<formInfo.ChangeSceneAnimationStateRequest>): void--><!--Device-formHost-function onChangeSceneAnimationState(callback: Callback<formInfo.ChangeSceneAnimationStateRequest>): void-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;formInfo.ChangeSceneAnimationStateRequest&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
