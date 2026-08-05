# off (System API)

## off('touch')

```TypeScript
function off(type: 'touch', receiver?: TouchEventReceiver): void
```

Cancels listening for global touchscreen input events. This API uses an asynchronous callback to return the result.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Required permissions:** ohos.permission.INPUT_MONITORING

<!--Device-inputMonitor-function off(type: 'touch', receiver?: TouchEventReceiver): void--><!--Device-inputMonitor-function off(type: 'touch', receiver?: TouchEventReceiver): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputMonitor

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'touch' | Yes | Event type. This field has a fixed value of **touch**. |
| receiver | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Callback for which listening is disabled. If this parameter is not specified, listening will be disabled for all callbacks registered by the current application. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_2. Incorrect parameter types; 3. Parameter verification failed. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission denied, non-system app called system api.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 12 and later |

**Example**

```TypeScript
import { inputMonitor } from '@kit.InputKit';
import { TouchEvent } from '@kit.InputKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          // Disable listening for a single callback.
          let callback = (touchEvent: TouchEvent) => {
            console.info(`Monitor on success ${JSON.stringify(touchEvent)}`);
            return false;
          };
          try {
            inputMonitor.on('touch', callback);
            inputMonitor.off('touch', callback);
            console.info(`Monitor off success`);
          } catch (error) {
            console.error(`Monitor execute failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

```TypeScript
import { inputMonitor } from '@kit.InputKit';
import { TouchEvent } from '@kit.InputKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          // Cancel listening for all callbacks.
          let callback = (touchEvent: TouchEvent) => {
            console.info(`Monitor on success ${JSON.stringify(touchEvent)}`);
            return false;
          };
          try {
            inputMonitor.on('touch', callback);
            inputMonitor.off('touch');
            console.info(`Monitor off success`);
          } catch (error) {
            console.error(`Monitor execute failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```


## off('mouse')

```TypeScript
function off(type: 'mouse', receiver?: Callback<MouseEvent>): void
```

Disables listening for global mouse events. This API uses an asynchronous callback to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Required permissions:** ohos.permission.INPUT_MONITORING

<!--Device-inputMonitor-function off(type: 'mouse', receiver?: Callback<MouseEvent>): void--><!--Device-inputMonitor-function off(type: 'mouse', receiver?: Callback<MouseEvent>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputMonitor

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'mouse' | Yes | Event type. This field has a fixed value of **mouse**. |
| receiver | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;\_\_\_MD\_LINK\_USD\_1\_\_\_&gt; | No | Callback for which listening is disabled. If this parameter is not specified, listening will be disabled for all callbacks registered by the current application. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_2. Incorrect parameter types; 3. Parameter verification failed. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission denied, non-system app called system api.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 12 and later |

**Example**

```TypeScript
import { inputMonitor } from '@kit.InputKit';
import { MouseEvent } from '@kit.InputKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          // Disable listening for a single callback.
          let callback = (mouseEvent: MouseEvent) => {
            console.info(`Monitor on success ${JSON.stringify(mouseEvent)}`);
            return false;
          };
          try {
            inputMonitor.on('mouse', callback);
            inputMonitor.off('mouse', callback);
            console.info(`Monitor off success`);
          } catch (error) {
            console.error(`Monitor execute failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

```TypeScript
import { inputMonitor } from '@kit.InputKit';
import { MouseEvent } from '@kit.InputKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          // Cancel listening for all callbacks.
          let callback = (mouseEvent: MouseEvent) => {
            console.info(`Monitor on success ${JSON.stringify(mouseEvent)}`);
            return false;
          };
          try {
            inputMonitor.on('mouse', callback);
            inputMonitor.off('mouse');
            console.info(`Monitor off success`);
          } catch (error) {
            console.error(`Monitor execute failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```


## off('pinch')

```TypeScript
function off(type: 'pinch', receiver?: Callback<Pinch>): void
```

Disables listening for global touchpad pinch events. This API uses an asynchronous callback to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Required permissions:** ohos.permission.INPUT_MONITORING

<!--Device-inputMonitor-function off(type: 'pinch', receiver?: Callback<Pinch>): void--><!--Device-inputMonitor-function off(type: 'pinch', receiver?: Callback<Pinch>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputMonitor

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'pinch' | Yes | Event type. This field has a fixed value of **pinch**. |
| receiver | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;Pinch&gt; | No | Callback for which listening is disabled. If this parameter is not specified,listening will be disabled for all callbacks registered by the current application. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | SystemAPI permit error. |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_2. Incorrect parameter types; 3. Parameter verification failed. |


## off('pinch')

```TypeScript
function off(type: 'pinch', fingers: number, receiver?: Callback<Pinch>): void
```

Disables listening for global touchpad pinch events. This API uses an asynchronous callback to return the result.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Required permissions:** ohos.permission.INPUT_MONITORING

<!--Device-inputMonitor-function off(type: 'pinch', fingers: number, receiver?: Callback<Pinch>): void--><!--Device-inputMonitor-function off(type: 'pinch', fingers: number, receiver?: Callback<Pinch>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputMonitor

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'pinch' | Yes | Event type. This field has a fixed value of **pinch**. |
| fingers | number | Yes | Number of fingers that trigger the pinch. The value must be greater than or equal to **2**. |
| receiver | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;Pinch&gt; | No | Callback for which listening is disabled. If this parameter is not specified,listening will be disabled for all callbacks registered by the current application. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | SystemAPI permit error. |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

```TypeScript
import { inputMonitor } from '@kit.InputKit';
import { Pinch } from '@kit.InputKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          // Disable listening for a single callback.
          let callback = (pinchEvent: Pinch) => {
            console.info(`Monitor on success ${JSON.stringify(pinchEvent)}`);
            return false;
          };
          try {
            inputMonitor.on('pinch', 2, callback);
            inputMonitor.off('pinch', 2, callback);
            console.info(`Monitor off success`);
          } catch (error) {
            console.error(`Monitor execute failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

```TypeScript
import { inputMonitor } from '@kit.InputKit';
import { Pinch } from '@kit.InputKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          // Cancel listening for all callbacks.
          let callback = (pinchEvent: Pinch) => {
            console.info(`Monitor on success ${JSON.stringify(pinchEvent)}`);
            return false;
          };
          try {
            inputMonitor.on('pinch', 2, callback);
            inputMonitor.off('pinch', 2);
            console.info(`Monitor off success`);
          } catch (error) {
            console.error(`Monitor execute failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```


## off('rotate')

```TypeScript
function off(type: 'rotate', fingers: number, receiver?: Callback<Rotate>): void
```

Disables listening for rotation events of the touchpad. This API uses an asynchronous callback to return the result.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Required permissions:** ohos.permission.INPUT_MONITORING

<!--Device-inputMonitor-function off(type: 'rotate', fingers: number, receiver?: Callback<Rotate>): void--><!--Device-inputMonitor-function off(type: 'rotate', fingers: number, receiver?: Callback<Rotate>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputMonitor

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'rotate' | Yes | Event type. This field has a fixed value of **rotate**. |
| fingers | number | Yes | Number of fingers that trigger a rotation. The value must not be greater than **2**. |
| receiver | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;Rotate&gt; | No | Callback for which listening is disabled. If this parameter is not specified, listening will be disabled for all callbacks registered by the current application. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | SystemAPI permit error. |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

```TypeScript
import { inputMonitor } from '@kit.InputKit';
import { Rotate } from '@kit.InputKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          // Disable listening for a single callback.
          let callback = (rotateEvent: Rotate) => {
            console.info(`Monitor on success ${JSON.stringify(rotateEvent)}`);
            return false;
          };
          try {
            inputMonitor.on('rotate', 2, callback);
            inputMonitor.off('rotate', 2, callback);
            console.info(`Monitor off success`);
          } catch (error) {
            console.error(`Monitor execute failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

```TypeScript
import { inputMonitor } from '@kit.InputKit';
import { Rotate } from '@kit.InputKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          // Cancel listening for all callbacks.
          let callback = (rotateEvent: Rotate) => {
            console.info(`Monitor on success ${JSON.stringify(rotateEvent)}`);
            return false;
          };
          try {
            inputMonitor.on('rotate', 2, callback);
            inputMonitor.off('rotate', 2);
            console.info(`Monitor off success`);
          } catch (error) {
            console.error(`Monitor execute failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```


## off('threeFingersSwipe')

```TypeScript
function off(type: 'threeFingersSwipe', receiver?: Callback<ThreeFingersSwipe>): void
```

Disables listening for three-finger swipe events. This API uses an asynchronous callback to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Required permissions:** ohos.permission.INPUT_MONITORING

<!--Device-inputMonitor-function off(type: 'threeFingersSwipe', receiver?: Callback<ThreeFingersSwipe>): void--><!--Device-inputMonitor-function off(type: 'threeFingersSwipe', receiver?: Callback<ThreeFingersSwipe>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputMonitor

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'threeFingersSwipe' | Yes | Event type. This field has a fixed value of **threeFingersSwipe**. |
| receiver | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;ThreeFingersSwipe&gt; | No | Callback for which listening is disabled. If this parameter is not specified, listening will be disabled for all callbacks registered by the current application. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | SystemAPI permit error. |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_2. Incorrect parameter types; 3. Parameter verification failed. |


## off('fourFingersSwipe')

```TypeScript
function off(type: 'fourFingersSwipe', receiver?: Callback<FourFingersSwipe>): void
```

Disables listening for four-finger swipe events. This API uses an asynchronous callback to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Required permissions:** ohos.permission.INPUT_MONITORING

<!--Device-inputMonitor-function off(type: 'fourFingersSwipe', receiver?: Callback<FourFingersSwipe>): void--><!--Device-inputMonitor-function off(type: 'fourFingersSwipe', receiver?: Callback<FourFingersSwipe>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputMonitor

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'fourFingersSwipe' | Yes | Event type. This field has a fixed value of **fourFingersSwipe**. |
| receiver | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;FourFingersSwipe&gt; | No | Callback for which listening is disabled. If this parameter is not specified, listening will be disabled for all callbacks registered by the current application. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | SystemAPI permit error. |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_2. Incorrect parameter types; 3. Parameter verification failed. |


## off('threeFingersTap')

```TypeScript
function off(type: 'threeFingersTap', receiver?: Callback<ThreeFingersTap>): void
```

Disables listening for three-finger tap events. This API uses an asynchronous callback to return the result.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Required permissions:** ohos.permission.INPUT_MONITORING

<!--Device-inputMonitor-function off(type: 'threeFingersTap', receiver?: Callback<ThreeFingersTap>): void--><!--Device-inputMonitor-function off(type: 'threeFingersTap', receiver?: Callback<ThreeFingersTap>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputMonitor

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'threeFingersTap' | Yes | Event type. This field has a fixed value of **threeFingersTap**. |
| receiver | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;ThreeFingersTap&gt; | No | Callback for which listening is disabled. If this parameter is not specified, listening will be disabled for all callbacks registered by the current application. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | SystemAPI permit error. |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_2. Incorrect parameter types; 3. Parameter verification failed. |


## off('fingerprint')

```TypeScript
function off(type: 'fingerprint', receiver?: Callback<FingerprintEvent>): void
```

Disables listening for fingerprint gesture input events. This API uses an asynchronous callback to return the result.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Required permissions:** ohos.permission.INPUT_MONITORING

<!--Device-inputMonitor-function off(type: 'fingerprint', receiver?: Callback<FingerprintEvent>): void--><!--Device-inputMonitor-function off(type: 'fingerprint', receiver?: Callback<FingerprintEvent>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputMonitor

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'fingerprint' | Yes | Input event type. The value is **fingerprint**. |
| receiver | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;FingerprintEvent&gt; | No | Callback for which listening is disabled. If this parameter is not specified, listening will be disabled for all callbacks registered by the current application. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | SystemAPI permit error. |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

```TypeScript
import { inputMonitor } from '@kit.InputKit';
import { FingerprintEvent } from '@kit.InputKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          // Disable listening for a single callback.
          let callback = (fingerprintEvent: FingerprintEvent) => {
            console.info(`Monitor on success ${JSON.stringify(fingerprintEvent)}`);
            return false;
          };
          try {
            inputMonitor.on('fingerprint', callback);
            inputMonitor.off("fingerprint", callback);
            console.info(`Monitor off success`);
          } catch (error) {
            console.error(`Monitor execute failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

```TypeScript
import { inputMonitor } from '@kit.InputKit';
import { FingerprintEvent } from '@kit.InputKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          // Cancel listening for all callbacks.
          let callback = (fingerprintEvent: FingerprintEvent) => {
            console.info(`Monitor on success ${JSON.stringify(fingerprintEvent)}`);
            return false;
          };
          try {
            inputMonitor.on('fingerprint', callback);
            inputMonitor.off("fingerprint");
            console.info(`Monitor off success`);
          } catch (error) {
            console.error(`Monitor execute failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```


## off('swipeInward')

```TypeScript
function off(type: 'swipeInward', receiver?: Callback<SwipeInward>): void
```

Cancels listening for inward swipe events. This API uses an asynchronous callback to return the result.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Required permissions:** ohos.permission.INPUT_MONITORING

<!--Device-inputMonitor-function off(type: 'swipeInward', receiver?: Callback<SwipeInward>): void--><!--Device-inputMonitor-function off(type: 'swipeInward', receiver?: Callback<SwipeInward>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputMonitor

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'swipeInward' | Yes | Input event type. The value is fixed at **SwipeInward**. |
| receiver | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;SwipeInward&gt; | No | Callback for which listening is disabled. If this parameter is not specified, listening will be disabled for all callbacks registered by the current application. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | SystemAPI permit error. |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. |

**Example**

```TypeScript
import { inputMonitor, SwipeInward } from '@kit.InputKit';

@Entry
@Component
struct Index {
build() {
  RelativeContainer() {
    Text()
      .onClick(() => {
        // Disable listening for a single callback.
        let callback = (swipeInward: SwipeInward) => {
          console.info(`Monitor on success ${JSON.stringify(swipeInward)}`);
          return false;
        };
        try {
          inputMonitor.on('swipeInward', callback);
          inputMonitor.off("swipeInward", callback);
          console.info(`Monitor off success`);
        } catch (error) {
          console.error(`Monitor execute failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
        }
      })
  }
}
}
```

```TypeScript
import { inputMonitor, SwipeInward } from '@kit.InputKit';

@Entry
@Component
struct Index {
build() {
  RelativeContainer() {
    Text()
      .onClick(() => {
        // Cancel listening for all callbacks.
        let callback = (swipeInward: SwipeInward) => {
          console.info(`Monitor on success ${JSON.stringify(swipeInward)}`);
          return false;
        };
        try {
          inputMonitor.on('swipeInward', callback);
          inputMonitor.off("swipeInward");
          console.info(`Monitor off success`);
        } catch (error) {
          console.error(`Monitor execute failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
        }
      })
  }
}
}
```


## off('touchscreenSwipe')

```TypeScript
function off(type: 'touchscreenSwipe', fingers: number, receiver?: Callback<TouchGestureEvent>): void
```

Disables listening for touchscreen swipe events. This API uses an asynchronous callback to return the result.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Required permissions:** ohos.permission.INPUT_MONITORING

<!--Device-inputMonitor-function off(type: 'touchscreenSwipe', fingers: number, receiver?: Callback<TouchGestureEvent>): void--><!--Device-inputMonitor-function off(type: 'touchscreenSwipe', fingers: number, receiver?: Callback<TouchGestureEvent>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputMonitor

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'touchscreenSwipe' | Yes | Event type. This field has a fixed value of **touchscreenSwipe**. |
| fingers | number | Yes | Number of fingers that trigger the swipe. The value range is [3, 5]. |
| receiver | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;TouchGestureEvent&gt; | No | Callback for which listening is disabled. If this parameter is not specified, listening will be disabled for all callbacks registered by the current application. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Caller is not a system application. |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types.3.Parameter verification failed. |

**Example**

```TypeScript
import { inputMonitor } from '@kit.InputKit';
import { TouchGestureEvent } from '@kit.InputKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          // Disable listening for a single callback.
          let callback = (event: TouchGestureEvent) => {
            console.info(`Monitor on success ${JSON.stringify(event)}`);
          };
          let fingers: number = 4;
          try {
            inputMonitor.on('touchscreenSwipe', fingers, callback);
            inputMonitor.off('touchscreenSwipe', fingers, callback);
          } catch (error) {
            console.error(`Monitor execute failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

```TypeScript
import { inputMonitor } from '@kit.InputKit';
import { TouchGestureEvent } from '@kit.InputKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          // Cancel listening for all callbacks.
          let fingers: number = 4;
          try {
            inputMonitor.on('touchscreenSwipe', fingers, (event: TouchGestureEvent) => {
              console.info(`Monitor on success ${JSON.stringify(event)}`);
            });
            inputMonitor.off('touchscreenSwipe', fingers);
          } catch (error) {
            console.error(`Monitor execute failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```


## off('touchscreenPinch')

```TypeScript
function off(type: 'touchscreenPinch', fingers: number, receiver?: Callback<TouchGestureEvent>): void
```

Disables listening for touchscreen pinch events. This API uses an asynchronous callback to return the result.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Required permissions:** ohos.permission.INPUT_MONITORING

<!--Device-inputMonitor-function off(type: 'touchscreenPinch', fingers: number, receiver?: Callback<TouchGestureEvent>): void--><!--Device-inputMonitor-function off(type: 'touchscreenPinch', fingers: number, receiver?: Callback<TouchGestureEvent>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputMonitor

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'touchscreenPinch' | Yes | Event type. This field has a fixed value of **touchscreenPinch**. |
| fingers | number | Yes | Number of fingers that trigger the pinch. The value range is [4, 5]. |
| receiver | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;TouchGestureEvent&gt; | No | Callback for which listening is disabled. If this parameter is not specified, listening will be disabled for all callbacks registered by the current application. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Caller is not a system application. |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types.3.Parameter verification failed. |

**Example**

```TypeScript
import { inputMonitor } from '@kit.InputKit';
import { TouchGestureEvent } from '@kit.InputKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          // Disable listening for a single callback.
          let callback = (event: TouchGestureEvent) => {
            console.info(`Monitor on success ${JSON.stringify(event)}`);
          };
          let fingers: number = 4;
          try {
            inputMonitor.on('touchscreenPinch', fingers, callback);
            inputMonitor.off("touchscreenPinch", fingers, callback);
          } catch (error) {
            console.error(`Monitor execute failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

```TypeScript
import { inputMonitor } from '@kit.InputKit';
import { TouchGestureEvent } from '@kit.InputKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          // Cancel listening for all callbacks.
          let fingers: number = 4;
          try {
            inputMonitor.on('touchscreenPinch', fingers, (event: TouchGestureEvent) => {
              console.info(`Monitor on success ${JSON.stringify(event)}`);
            });
            inputMonitor.off("touchscreenPinch", fingers);
          } catch (error) {
            console.error(`Monitor execute failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```


## off('keyPressed')

```TypeScript
function off(type: 'keyPressed', receiver?: Callback<KeyEvent>): void
```

Cancels listening for the press and release events of the specified key, which can be the **META\_LEFT**, **META\_RIGHT**, power, or volume key. This API must be used together with **inputMonitor.on ('keyPressed')**. This API uses an asynchronous callback to return the result.

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Required permissions:** ohos.permission.INPUT_MONITORING

<!--Device-inputMonitor-function off(type: 'keyPressed', receiver?: Callback<KeyEvent>): void--><!--Device-inputMonitor-function off(type: 'keyPressed', receiver?: Callback<KeyEvent>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputMonitor

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'keyPressed' | Yes | Event type. This parameter has a fixed value of **keyPressed**. |
| receiver | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;\_\_\_MD\_LINK\_USD\_1\_\_\_&gt; | No | Callback for which listening is disabled. If this parameter is not specified, listening will be disabled for all callbacks registered by the current application. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission denied, non-system app called system api. |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

```TypeScript
import { inputMonitor, KeyEvent, KeyCode } from '@kit.InputKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          // Disable listening for a single callback.
          try {
            let callback = (event: KeyEvent) => {
              console.info(`Monitor on success ${JSON.stringify(event)}`);
            };
            let keys: Array<KeyCode> = [KeyCode.KEYCODE_VOLUME_UP];
            inputMonitor.on('keyPressed', keys, callback);
            inputMonitor.off("keyPressed", callback);
          } catch (error) {
            console.error(`Monitor execute failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

```TypeScript
import { inputMonitor, KeyEvent, KeyCode } from '@kit.InputKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          // Cancel listening for all callbacks.
          try {
            let keys: Array<KeyCode> = [KeyCode.KEYCODE_VOLUME_UP];
            inputMonitor.on('keyPressed', keys, (event: KeyEvent) => {
              console.info(`Monitor on success ${JSON.stringify(event)}`);
            });
            inputMonitor.off("keyPressed");
          } catch (error) {
            console.error(`Monitor execute failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

