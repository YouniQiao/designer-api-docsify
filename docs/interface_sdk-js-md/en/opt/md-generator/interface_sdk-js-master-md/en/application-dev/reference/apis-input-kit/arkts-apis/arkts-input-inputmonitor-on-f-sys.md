# on (System API)

## Modules to Import

```TypeScript
import { inputMonitor } from 'kits/@kit.InputKit';
```

## on('touch')

```TypeScript
function on(type: 'touch', receiver: TouchEventReceiver): void
```

Listens for global touchscreen input events. This API uses an asynchronous callback to return the result.

**Since:** 7

**Required permissions:** ohos.permission.INPUT_MONITORING

<!--Device-inputMonitor-function on(type: 'touch', receiver: TouchEventReceiver): void--><!--Device-inputMonitor-function on(type: 'touch', receiver: TouchEventReceiver): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputMonitor

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'touch' | Yes |
| receiver | [TouchEventReceiver](arkts-input-inputmonitor-toucheventreceiver-t-sys.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

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
          try {
            // Subscribe to Touch Events
            inputMonitor.on('touch', (touchEvent: TouchEvent) => {
              console.info(`Succeeded in monitoring on ${JSON.stringify(touchEvent)}.`);
              return false;
            });
          } catch (error) {
            console.error(`Failed to monitor the touch screen event, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```


## on('mouse')

```TypeScript
function on(type: 'mouse', receiver: Callback<MouseEvent>): void
```

Enables listening for global mouse events. This API uses an asynchronous callback to return the result.

**Since:** 9

**Required permissions:** ohos.permission.INPUT_MONITORING

<!--Device-inputMonitor-function on(type: 'mouse', receiver: Callback<MouseEvent>): void--><!--Device-inputMonitor-function on(type: 'mouse', receiver: Callback<MouseEvent>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputMonitor

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'mouse' | Yes |
| receiver | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[MouseEvent](arkts-input-multimodalinput-mouseevent-mouseevent-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

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
          try {
            // Subscribe to Mouse Events
            inputMonitor.on('mouse', (mouseEvent: MouseEvent) => {
              console.info(`Succeeded in monitoring on ${JSON.stringify(mouseEvent)}.`);
              return false;
            });
          } catch (error) {
            console.error(`Failed to monitor the mouse event, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```


## on('mouse')

```TypeScript
function on(type: 'mouse', rect: display.Rect[], receiver: Callback<MouseEvent>): void
```

Enables listening for mouse events. When the mouse pointer moves to the specified rectangular area, a callback is triggered. This API uses an asynchronous callback to return the result.

**Since:** 11

**Required permissions:** ohos.permission.INPUT_MONITORING

<!--Device-inputMonitor-function on(type: 'mouse', rect: display.Rect[], receiver: Callback<MouseEvent>): void--><!--Device-inputMonitor-function on(type: 'mouse', rect: display.Rect[], receiver: Callback<MouseEvent>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputMonitor

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'mouse' | Yes |
| rect | display.Rect[] | Yes |
| receiver | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[MouseEvent](arkts-input-multimodalinput-mouseevent-mouseevent-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { inputMonitor } from '@kit.InputKit';
import { MouseEvent } from '@kit.InputKit';
import { display } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          /**
           * Callback triggered when the mouse pointer moves to the specified rectangular area.
           */
          let callback = (mouseEvent : MouseEvent) => {
            this.getUIContext().getPromptAction().showToast({
              message: `Monitor on success: ${JSON.stringify(mouseEvent)}`
            })
            console.info(`Succeeded in monitoring on ${JSON.stringify(mouseEvent)}.`);
            return false;
          };

          /**
           * Rectangular area where a callback is triggered.
           */
          let rect: display.Rect[] = [{
            left: 100,
            top: 100,
            width: 100,
            height: 100
          }, {
            left: 600,
            top: 100,
            width: 100,
            height: 100
          }];

          try {
            // Subscribe to Mouse Events
            inputMonitor.on('mouse', rect, callback);
          } catch (error) {
            console.error(`Failed to monitor the mouse event, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```


## on('pinch')

```TypeScript
function on(type: 'pinch', receiver: Callback<Pinch>): void
```

Enables listening for global touchpad pinch events. This API uses an asynchronous callback to return the result.

**Since:** 10

**Required permissions:** ohos.permission.INPUT_MONITORING

<!--Device-inputMonitor-function on(type: 'pinch', receiver: Callback<Pinch>): void--><!--Device-inputMonitor-function on(type: 'pinch', receiver: Callback<Pinch>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputMonitor

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'pinch' | Yes |
| receiver | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[Pinch](arkts-input-multimodalinput-gestureevent-pinch-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { inputMonitor } from '@kit.InputKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          try {
            // Subscribe to Pinch Event
            inputMonitor.on('pinch', (pinchEvent) => {
              console.info(`Succeeded in monitoring on ${JSON.stringify(pinchEvent)}.`);
              return false;
            });
          } catch (error) {
            console.error(`Failed to monitor the pinch event, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```


## on('pinch')

```TypeScript
function on(type: 'pinch', fingers: number, receiver: Callback<Pinch>): void
```

Enables listening for global touchpad pinch events. This API uses an asynchronous callback to return the result.

**Since:** 11

**Required permissions:** ohos.permission.INPUT_MONITORING

<!--Device-inputMonitor-function on(type: 'pinch', fingers: number, receiver: Callback<Pinch>): void--><!--Device-inputMonitor-function on(type: 'pinch', fingers: number, receiver: Callback<Pinch>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputMonitor

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'pinch' | Yes |
| fingers | number | Yes |
| receiver | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[Pinch](arkts-input-multimodalinput-gestureevent-pinch-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

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
          try {
            // Number of fingers for pinch gesture monitoring: 2
            inputMonitor.on('pinch', 2, (pinchEvent: Pinch) => {
              console.info(`Succeeded in monitoring on ${JSON.stringify(pinchEvent)}.`);
              return false;
            });
          } catch (error) {
            console.error(`Failed to monitor pinch event, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```


## on('rotate')

```TypeScript
function on(type: 'rotate', fingers: number, receiver: Callback<Rotate>): void
```

Enables listening for rotation events of the touchpad. This API uses an asynchronous callback to return the result.

**Since:** 11

**Required permissions:** ohos.permission.INPUT_MONITORING

<!--Device-inputMonitor-function on(type: 'rotate', fingers: number, receiver: Callback<Rotate>): void--><!--Device-inputMonitor-function on(type: 'rotate', fingers: number, receiver: Callback<Rotate>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputMonitor

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'rotate' | Yes |
| fingers | number | Yes |
| receiver | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[Rotate](arkts-input-multimodalinput-gestureevent-rotate-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

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
          try {
            // Number of Fingers for Rotation Gesture Monitoring: 2
            inputMonitor.on('rotate', 2, (rotateEvent: Rotate) => {
              console.info(`Succeeded in monitoring on ${JSON.stringify(rotateEvent)}.`);
              return false;
            });
          } catch (error) {
            console.error(`Failed to monitor rotate event, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```


## on('threeFingersSwipe')

```TypeScript
function on(type: 'threeFingersSwipe', receiver: Callback<ThreeFingersSwipe>): void
```

Enables listening for three-finger swipe events. This API uses an asynchronous callback to return the result.

**Since:** 10

**Required permissions:** ohos.permission.INPUT_MONITORING

<!--Device-inputMonitor-function on(type: 'threeFingersSwipe', receiver: Callback<ThreeFingersSwipe>): void--><!--Device-inputMonitor-function on(type: 'threeFingersSwipe', receiver: Callback<ThreeFingersSwipe>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputMonitor

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'threeFingersSwipe' | Yes |
| receiver | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ThreeFingersSwipe](arkts-input-multimodalinput-gestureevent-threefingersswipe-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { inputMonitor } from '@kit.InputKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          try {
            // Subscribe to Three-Finger Swipe Events
            inputMonitor.on('threeFingersSwipe', (threeFingersSwipe) => {
              console.info(`Succeeded in monitoring on ${JSON.stringify(threeFingersSwipe)}.`);
              return false;
            });
          } catch (error) {
            console.error(`Failed to monitor three fingers swipe, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```


## on('fourFingersSwipe')

```TypeScript
function on(type: 'fourFingersSwipe', receiver: Callback<FourFingersSwipe>): void
```

Enables listening for four-finger swipe events. This API uses an asynchronous callback to return the result.

**Since:** 10

**Required permissions:** ohos.permission.INPUT_MONITORING

<!--Device-inputMonitor-function on(type: 'fourFingersSwipe', receiver: Callback<FourFingersSwipe>): void--><!--Device-inputMonitor-function on(type: 'fourFingersSwipe', receiver: Callback<FourFingersSwipe>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputMonitor

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'fourFingersSwipe' | Yes |
| receiver | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[FourFingersSwipe](arkts-input-multimodalinput-gestureevent-fourfingersswipe-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { inputMonitor } from '@kit.InputKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          try {
            // Subscribe to Four-Finger Swipe Events
            inputMonitor.on('fourFingersSwipe', (fourFingersSwipe) => {
              console.info(`Succeeded in monitoring on ${JSON.stringify(fourFingersSwipe)}.`);
              return false;
            });
          } catch (error) {
            console.error(`Failed to monitor four fingers swipe, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```


## on('threeFingersTap')

```TypeScript
function on(type: 'threeFingersTap', receiver: Callback<ThreeFingersTap>): void
```

Enables listening for three-finger tap events. This API uses an asynchronous callback to return the result.

**Since:** 11

**Required permissions:** ohos.permission.INPUT_MONITORING

<!--Device-inputMonitor-function on(type: 'threeFingersTap', receiver: Callback<ThreeFingersTap>): void--><!--Device-inputMonitor-function on(type: 'threeFingersTap', receiver: Callback<ThreeFingersTap>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputMonitor

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'threeFingersTap' | Yes |
| receiver | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ThreeFingersTap](arkts-input-multimodalinput-gestureevent-threefingerstap-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { inputMonitor } from '@kit.InputKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          try {
            // Subscribe to Three-Finger Tap Event
            inputMonitor.on('threeFingersTap', (threeFingersTap) => {
              console.info(`Succeeded in monitoring on ${JSON.stringify(threeFingersTap)}.`);
              return false;
            });
          } catch (error) {
            console.error(`Failed to monitor three fingers tap, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```


## on('fingerprint')

```TypeScript
function on(type: 'fingerprint', receiver: Callback<FingerprintEvent>): void
```

Enables listening for fingerprint gesture input events. This API uses an asynchronous callback to return the result.

**Since:** 12

**Required permissions:** ohos.permission.INPUT_MONITORING

<!--Device-inputMonitor-function on(type: 'fingerprint', receiver: Callback<FingerprintEvent>): void--><!--Device-inputMonitor-function on(type: 'fingerprint', receiver: Callback<FingerprintEvent>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputMonitor

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'fingerprint' | Yes |
| receiver | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[FingerprintEvent](arkts-input-multimodalinput-shortkey-fingerprintevent-i-sys.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { inputMonitor } from '@kit.InputKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          try {
            // Subscribe to Fingerprint Events
            inputMonitor.on('fingerprint', (FingerprintEvent) => {
              console.info(`Succeeded in monitoring on ${JSON.stringify(FingerprintEvent)}.`);
              return false;
            });
          } catch (error) {
            console.error(`Failed to monitor finger print event, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```


## on('swipeInward')

```TypeScript
function on(type: 'swipeInward', receiver: Callback<SwipeInward>): void
```

Listens for inward swipe events. This API uses an asynchronous callback to return the result.

**Since:** 12

**Required permissions:** ohos.permission.INPUT_MONITORING

<!--Device-inputMonitor-function on(type: 'swipeInward', receiver: Callback<SwipeInward>): void--><!--Device-inputMonitor-function on(type: 'swipeInward', receiver: Callback<SwipeInward>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputMonitor

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'swipeInward' | Yes |
| receiver | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SwipeInward](arkts-input-multimodalinput-gestureevent-swipeinward-i-sys.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { inputMonitor } from '@kit.InputKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          try {
            // Subscribe to Swipe Inward Event
            inputMonitor.on('swipeInward', (SwipeInward) => {
              console.info(`Succeeded in monitoring on ${JSON.stringify(SwipeInward)}.`);
              return false;
            });
          } catch (error) {
            console.error(`Failed to monitor swipe inward, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```


## on('touchscreenSwipe')

```TypeScript
function on(type: 'touchscreenSwipe', fingers: number, receiver: Callback<TouchGestureEvent>): void
```

Enables listening for touchscreen swipe events. This API uses an asynchronous callback to return the result.

**Since:** 18

**Required permissions:** ohos.permission.INPUT_MONITORING

<!--Device-inputMonitor-function on(type: 'touchscreenSwipe', fingers: number, receiver: Callback<TouchGestureEvent>): void--><!--Device-inputMonitor-function on(type: 'touchscreenSwipe', fingers: number, receiver: Callback<TouchGestureEvent>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputMonitor

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'touchscreenSwipe' | Yes |
| fingers | number | Yes |
| receiver | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[TouchGestureEvent](arkts-input-multimodalinput-gestureevent-touchgestureevent-i-sys.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

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
          let fingers: number = 4;
          try {
            // Subscribe to Touchscreen Swipe Events
            inputMonitor.on('touchscreenSwipe', fingers, (event: TouchGestureEvent) => {
              console.info(`Succeeded in monitoring on ${JSON.stringify(event)}.`);
            });
          } catch (error) {
            console.error(`Failed to monitor touch screen swipe, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```


## on('touchscreenPinch')

```TypeScript
function on(type: 'touchscreenPinch', fingers: number, receiver: Callback<TouchGestureEvent>): void
```

Enables listening for touchscreen pinch events. This API uses an asynchronous callback to return the result.

**Since:** 18

**Required permissions:** ohos.permission.INPUT_MONITORING

<!--Device-inputMonitor-function on(type: 'touchscreenPinch', fingers: number, receiver: Callback<TouchGestureEvent>): void--><!--Device-inputMonitor-function on(type: 'touchscreenPinch', fingers: number, receiver: Callback<TouchGestureEvent>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputMonitor

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'touchscreenPinch' | Yes |
| fingers | number | Yes |
| receiver | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[TouchGestureEvent](arkts-input-multimodalinput-gestureevent-touchgestureevent-i-sys.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

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
          let fingers: number = 4;
          try {
            // Subscribe to Touchscreen Pinch Event
            inputMonitor.on('touchscreenPinch', fingers, (event: TouchGestureEvent) => {
              console.info(`Succeeded in monitoring on ${JSON.stringify(event)}.`);
            });
          } catch (error) {
            console.error(`Failed to monitor touch screen pinch, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```


## on('keyPressed')

```TypeScript
function on(type: 'keyPressed', keys: Array<KeyCode>, receiver: Callback<KeyEvent>): void
```

Listens for the press and release events of the specified key, which can be the **META_LEFT**, **META_RIGHT**,power, or volume key. This API uses an asynchronous callback to return the result.

**Since:** 15

**Required permissions:** ohos.permission.INPUT_MONITORING

<!--Device-inputMonitor-function on(type: 'keyPressed', keys: Array<KeyCode>, receiver: Callback<KeyEvent>): void--><!--Device-inputMonitor-function on(type: 'keyPressed', keys: Array<KeyCode>, receiver: Callback<KeyEvent>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputMonitor

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'keyPressed' | Yes |
| keys | Array&lt;[KeyCode](arkts-input-multimodalinput-keycode-keycode-e.md)&gt; | Yes |
| receiver | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[KeyEvent](arkts-input-multimodalinput-keyevent-keyevent-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [4100001](../errorcode-inputmonitor.md#4100001-event-listening-not-supported-for-the-key) |

## Examples

```TypeScript
import { inputMonitor, KeyEvent, KeyCode } from '@kit.InputKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          try {
            let keys: Array<KeyCode> = [KeyCode.KEYCODE_VOLUME_UP];
            // Subscribe to Key Press Events
            inputMonitor.on('keyPressed', keys, (event: KeyEvent ) => {
              console.info(`Succeeded in monitoring on ${JSON.stringify(event)}.`);
            });
          } catch (error) {
            console.error(`Failed to monitor key pressed, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```
