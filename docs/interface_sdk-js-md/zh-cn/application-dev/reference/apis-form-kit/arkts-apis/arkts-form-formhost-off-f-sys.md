# off（系统接口）

## 导入模块

```TypeScript
import { formHost } from 'kits/@kit.FormKit';
```

## off("formUninstall")

```TypeScript
function off(type: "formUninstall", callback?: Callback<string>): void
```

取消订阅卡片卸载事件。使用callback异步回调。

> **说明：**&gt;
> 卡片卸载与卡片移除不同。当应用卸载时，对应的卡片会自动卸载。

**起始版本：** 9

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | "formUninstall" | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |


## off('formOverflow')

```TypeScript
function off(type: 'formOverflow', callback?: Callback<formInfo.OverflowRequest>): void
```

取消订阅互动卡片动效请求事件。使用callback异步回调。

**起始版本：** 20

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'formOverflow' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;formInfo.OverflowRequest&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |


## off('changeSceneAnimationState')

```TypeScript
function off(type: 'changeSceneAnimationState', 
    callback?: Callback<formInfo.ChangeSceneAnimationStateRequest>): void
```

取消订阅互动卡片状态切换请求事件。互动卡片状态分为激活态和非激活态，非激活态下，互动卡片同普通卡片一致；激活态下，互动卡片支持拉起卡片提供方所开发的LiveFormExtensionAbility进程，实现互动卡片动效。使用 callback异步回调。

**起始版本：** 20

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'changeSceneAnimationState' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;formInfo.ChangeSceneAnimationStateRequest&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |


## off('getFormRect')

```TypeScript
function off(type: 'getFormRect', callback?: formInfo.GetFormRectInfoCallback): void
```

取消订阅卡片位置尺寸查询请求事件。使用callback异步回调。

**起始版本：** 20

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'getFormRect' | 是 |
| callback | formInfo.GetFormRectInfoCallback | 否 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |


## off('getLiveFormStatus')

```TypeScript
function off(type: 'getLiveFormStatus', 
    callback?: formInfo.GetLiveFormStatusCallback): void
```

Cancels Listening to the event of get live form status.

**起始版本：** 20

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'getLiveFormStatus' | 是 |
| callback | formInfo.GetLiveFormStatusCallback | 否 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
