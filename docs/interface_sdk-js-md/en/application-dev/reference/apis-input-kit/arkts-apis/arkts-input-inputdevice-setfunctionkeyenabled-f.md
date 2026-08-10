# setFunctionKeyEnabled

## Modules to Import

```TypeScript
import { inputDevice } from 'kits/@kit.InputKit';
```

## setFunctionKeyEnabled

```TypeScript
function setFunctionKeyEnabled(functionKey: FunctionKey, enabled: boolean): Promise<void>
```

设置功能键（如：CapsLock键）使能状态。使用Promise异步回调。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.INPUT_KEYBOARD_CONTROLLER

<!--Device-inputDevice-function setFunctionKeyEnabled(functionKey: FunctionKey, enabled: boolean): Promise<void>--><!--Device-inputDevice-function setFunctionKeyEnabled(functionKey: FunctionKey, enabled: boolean): Promise<void>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputDevice

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| functionKey | [FunctionKey](arkts-input-inputdevice-functionkey-e.md) | Yes | 需要设置的功能键类型。 |
| enabled | boolean | Yes | 功能键使能状态。取值为true表示使能功能键，取值为false表示不使能功能键。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |
| 3900003 | It is prohibited for non-input applications. |
| 201 | Permission denied. |
| 3900002 | There is currently no keyboard device connected. |

## Examples

```TypeScript
import { inputDevice } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          try {
            // Set Function Key Enabled Status
            inputDevice.setFunctionKeyEnabled(inputDevice.FunctionKey.CAPS_LOCK, true).then(() => {
              console.info(`Succeeded in setting capslock state.`);
            }).catch((error: BusinessError) => {
              console.error(`Failed to set capslock state, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
            });
          } catch (error) {
            console.error(`Failed to set capslock enable, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```

