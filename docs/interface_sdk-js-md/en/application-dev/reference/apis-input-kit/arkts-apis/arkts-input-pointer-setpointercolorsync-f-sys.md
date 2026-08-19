# setPointerColorSync (System API)

## Modules to Import

```TypeScript
import { pointer } from '@kit.InputKit';
```

## setPointerColorSync

```TypeScript
function setPointerColorSync(color: int): void
```

Sets the pointer color. This API returns the result synchronously. &gt; **NOTE：**&gt; &gt; When performing this operation, you need to connect an external device, such as a mouse or Bluetooth device.

**Since:** 23

<!--Device-pointer-function setPointerColorSync(color: int): void--><!--Device-pointer-function setPointerColorSync(color: int): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Pointer

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| color | int | Yes | Pointer color. The default value is **black** (0x000000). |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; 3. Parameter verification failed. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | SystemAPI permission error. |

**Examples**

```TypeScript
import { pointer } from '@kit.InputKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          try {
            pointer.setPointerColorSync(0xF6C800);
            console.info(`setPointerColorSync success`);
          } catch (error) {
            console.error(`setPointerColorSync failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

