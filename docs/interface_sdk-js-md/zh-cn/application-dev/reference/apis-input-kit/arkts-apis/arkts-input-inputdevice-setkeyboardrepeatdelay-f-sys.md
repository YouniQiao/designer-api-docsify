# setKeyboardRepeatDelay（系统接口）

## 导入模块

```TypeScript
import { inputDevice } from 'kits/@kit.InputKit';
```

## setKeyboardRepeatDelay

```TypeScript
function setKeyboardRepeatDelay(delay: number, callback: AsyncCallback<void>): void
```

设置键盘按键的重复时延，使用callback异步回调。

**起始版本：** 10

**系统能力：** SystemCapability.MultimodalInput.Input.InputDevice

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| delay | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |


## setKeyboardRepeatDelay

```TypeScript
function setKeyboardRepeatDelay(delay: number): Promise<void>
```

设置键盘按键的重复时延，使用Promise异步回调。

**起始版本：** 10

**系统能力：** SystemCapability.MultimodalInput.Input.InputDevice

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| delay | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
