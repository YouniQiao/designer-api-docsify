# onAbilityFirstFrameStateChange（系统接口）

## 导入模块

```TypeScript
```

## onAbilityFirstFrameStateChange

```TypeScript
function onAbilityFirstFrameStateChange(observer: AbilityFirstFrameStateObserver, bundleName?: string): void
```

注册监听Ability首帧绘制完成事件观察者对象，可用于系统应用监听Ability首帧绘制事件。

**起始版本：** 23

**需要权限：** ohos.permission.RUNNING_STATE_OBSERVER

<!--Device-appManager-function onAbilityFirstFrameStateChange(observer: AbilityFirstFrameStateObserver, bundleName?: string): void--><!--Device-appManager-function onAbilityFirstFrameStateChange(observer: AbilityFirstFrameStateObserver, bundleName?: string): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [observer](../../apis-telephony-kit/arkts-apis/arkts-telephony-observer.md) | [AbilityFirstFrameStateObserver](arkts-ability-appmanager-abilityfirstframestateobserver-t-sys.md) | 是 |
| bundleName | string | 否 |

**错误码：**

| 错误码ID |
| --- |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
