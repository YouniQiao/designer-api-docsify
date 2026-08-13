# offKey（系统接口）

## offKey

```TypeScript
function offKey(keyOptions: KeyOptions, callback?: Callback<KeyOptions>): void
```

取消订阅系统快捷键。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-inputConsumer-function offKey(keyOptions: KeyOptions, callback?: Callback<KeyOptions>): void--><!--Device-inputConsumer-function offKey(keyOptions: KeyOptions, callback?: Callback<KeyOptions>): void-End-->

**系统能力：** SystemCapability.MultimodalInput.Input.InputConsumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| keyOptions | [KeyOptions](../../apis-test-kit/arkts-apis/arkts-test-uitest-keyoptions-i.md) | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;KeyOptions&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |


## offKey

```TypeScript
function offKey(keyOptions: KeyOptions, callback?: KeyCommandCallback): void
```

取消订阅系统快捷键。使用callback异步回调。

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-inputConsumer-function offKey(keyOptions: KeyOptions, callback?: KeyCommandCallback): void--><!--Device-inputConsumer-function offKey(keyOptions: KeyOptions, callback?: KeyCommandCallback): void-End-->

**系统能力：** SystemCapability.MultimodalInput.Input.InputConsumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| keyOptions | [KeyOptions](../../apis-test-kit/arkts-apis/arkts-test-uitest-keyoptions-i.md) | 是 |
| callback | [KeyCommandCallback](arkts-input-inputconsumer-keycommandcallback-t-sys.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { inputConsumer } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

let leftCtrlKey = 2072;
let cKey = 2049;
let callback: inputConsumer.KeyCommandCallback = (keyOptions, keyEvents): void => {
  console.info(`KeyEvent received`);
}
let keyOptions: inputConsumer.KeyOptions = {
  preKeys: [leftCtrlKey],
  finalKey: cKey,
  isFinalKeyDown: true,
  finalKeyDownDuration: 0,
  triggerType: inputConsumer.KeyCommandTriggerType.PRESSED
};
try {
  inputConsumer.onKey(keyOptions, callback);
  inputConsumer.offKey(keyOptions, callback);
  console.info(`Unsubscribe success`);
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`Failed to execute operation. Code: ${err.code}, message: ${err.message}`);
}
```

```TypeScript
import { inputConsumer } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

let leftCtrlKey = 2072;
let cKey = 2049;
let keyOptions: inputConsumer.KeyOptions = {
  preKeys: [leftCtrlKey],
  finalKey: cKey,
  isFinalKeyDown: true,
  finalKeyDownDuration: 0,
  triggerType: inputConsumer.KeyCommandTriggerType.PRESSED
};
try {
  inputConsumer.offKey(keyOptions);
  console.info(`Unsubscribe all success`);
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`Failed to execute operation. Code: ${err.code}, message: ${err.message}`);
}
```
