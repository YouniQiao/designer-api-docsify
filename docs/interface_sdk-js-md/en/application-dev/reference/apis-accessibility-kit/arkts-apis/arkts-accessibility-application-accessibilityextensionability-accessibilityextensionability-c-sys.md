# AccessibilityExtensionAbility

AccessibilityExtensionAbility provides the accessibility extension service capability based on the ExtensionAbility framework.

**Since:** 23

<!--Device-unnamed-declare class AccessibilityExtensionAbility--><!--Device-unnamed-declare class AccessibilityExtensionAbility-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

## Modules to Import

```TypeScript
import { AccessibilityElement } from 'AccessibilityElement';
import { AccessibilityExtensionContext } from 'AccessibilityExtensionContext';
import { ElementAttributeKeys } from 'ElementAttributeKeys';
import { ElementAttributeValues } from 'ElementAttributeValues';
import { FocusDirection } from 'FocusDirection';
import { FocusType } from 'FocusType';
import { Rect } from 'Rect';
import { WindowType } from 'WindowType';
import { AccessibilityEvent } from 'AccessibilityEvent';
import { AccessibilityEventInfo } from 'AccessibilityEventInfo';
import { Parameter } from 'Parameter';
import { FocusRule } from 'FocusRule';
import { FocusCondition } from 'FocusCondition';
import { FocusMoveResult } from 'FocusMoveResult';
import { AccessibilityVirtualNode } from 'AccessibilityVirtualNode';
import { TouchPosition } from 'TouchPosition';
```

## onAccessibilityConnect

```TypeScript
onAccessibilityConnect(): void
```

Callback invoked when the accessibility service is successfully connected. When the user enables AccessibilityExtensionAbility, the system service calls this API after the connection is established to notify the ability that it has been successfully connected. You can implement service logic initialization in this method. This API can be overridden as required.

**Since:** 23

**Required permissions:** ohos.permission.ACCESSIBILITY_EXTENSION_ABILITY

<!--Device-AccessibilityExtensionAbility-onAccessibilityConnect(): void--><!--Device-AccessibilityExtensionAbility-onAccessibilityConnect(): void-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed.The application does not have the permission required to call the API. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

**Examples**

```TypeScript
import { AccessibilityExtensionAbility } from '@kit.AccessibilityKit';

class MyAccessibilityExtensionAbility extends AccessibilityExtensionAbility {
  onAccessibilityConnect(): void {
    console.log('AxExtensionAbility onAccessibilityConnect');
  }
}
```

## onAccessibilityDisconnect

```TypeScript
onAccessibilityDisconnect(): void
```

Callback invoked when the accessibility service is successfully disconnected. When the user disables AccessibilityExtensionAbility, the system service calls this API after the disconnection is completed. You can implement resource reclamation and service exit operations in this method. This API can be overridden as required.

**Since:** 23

**Required permissions:** ohos.permission.ACCESSIBILITY_EXTENSION_ABILITY

<!--Device-AccessibilityExtensionAbility-onAccessibilityDisconnect(): void--><!--Device-AccessibilityExtensionAbility-onAccessibilityDisconnect(): void-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed.The application does not have the permission required to call the API. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

**Examples**

```TypeScript
import { AccessibilityExtensionAbility } from '@kit.AccessibilityKit';

class MyAccessibilityExtensionAbility extends AccessibilityExtensionAbility {
  onAccessibilityDisconnect(): void {
    console.log('AxExtensionAbility onAccessibilityDisconnect');
  }
}
```

## onAccessibilityEventInfo

```TypeScript
onAccessibilityEventInfo(event: AccessibilityEventInfo): void
```

When an accessibility event occurs, the system distributes the event to the connected AccessibilityExtensionAbility and calls this API. You can process service logic based on the event information. This API usually needs to be overridden. For details about event types, see [AccessibilityEventType](arkts-accessibility-accessibility-accessibilityeventtype-e-sys.md#accessibilityeventtype-system-api).

**Since:** 23

**Required permissions:** ohos.permission.ACCESSIBILITY_EXTENSION_ABILITY

<!--Device-AccessibilityExtensionAbility-onAccessibilityEventInfo(event: AccessibilityEventInfo): void--><!--Device-AccessibilityExtensionAbility-onAccessibilityEventInfo(event: AccessibilityEventInfo): void-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [AccessibilityEventInfo](arkts-accessibility-application-accessibilityextensionability-accessibilityeventinfo-i-sys.md) | Yes | Accessibility event information. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed.The application does not have the permission required to call the API. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

**Examples**

```TypeScript
import { AccessibilityExtensionAbility, AccessibilityEventInfo, AccessibilityEventType } from '@kit.AccessibilityKit';

class MyAccessibilityExtensionAbility extends AccessibilityExtensionAbility {
  onAccessibilityEventInfo(event: AccessibilityEventInfo): void {
    console.log('AxExtensionAbility onAccessibilityEventInfo');
    if (event.eventType === AccessibilityEventType.TYPE_CLICK) {
      console.log('AxExtensionAbility onAccessibilityEventInfo: click');
    }
  }
}
```

## onAccessibilityKeyEvent

```TypeScript
onAccessibilityKeyEvent(keyEvent: KeyEvent): boolean
```

Called when a key is pressed. You can determine whether to consume the event based on the service logic in this method. This API can be overridden as required.

**Since:** 23

**Required permissions:** ohos.permission.ACCESSIBILITY_EXTENSION_ABILITY

<!--Device-AccessibilityExtensionAbility-onAccessibilityKeyEvent(keyEvent: KeyEvent): boolean--><!--Device-AccessibilityExtensionAbility-onAccessibilityKeyEvent(keyEvent: KeyEvent): boolean-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| keyEvent | [KeyEvent](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-keyevent-keyevent-i.md) | Yes | Key event. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | The value **true** indicates that the event is consumed and will not be propagated. <br>The value **false** indicates that the event is not consumed and will continue to be propagated. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed.The application does not have the permission required to call the API. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

**Examples**

```TypeScript
import { AccessibilityExtensionAbility } from '@kit.AccessibilityKit';
import { KeyEvent, KeyCode } from '@kit.InputKit';

class MyAccessibilityExtensionAbility extends AccessibilityExtensionAbility {
  onAccessibilityKeyEvent(keyEvent: KeyEvent): boolean {
    console.log('AxExtensionAbility onAccessibilityKeyEvent');
    if (keyEvent.key.code === KeyCode.KEYCODE_VOLUME_UP) {
      console.log('AxExtensionAbility onAccessibilityKeyEvent: intercept 16');
      return true;
    }
    return false;
  }
}
```

