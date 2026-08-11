# @ohos.inputMethod.ExtraConfig(The extra config of edit box.)

This module manages input method extension information. It enables the ArkUI editor to pass such information to the
 input method application when the input method is launched. After processing the extension information, the input
 method application can retrieve the details added by the host application. The total length of the information cannot
 exceed 32 KB.


## Modules to Import

```TypeScript
import { InputMethodExtraConfig } from 'kits/@kit.IMEKit';
```

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [InputMethodExtraConfig](arkts-ime-inputmethod-extraconfig-inputmethodextraconfig-i.md) | Represents the extension information of an input method. |

### Types

| Name | Description |
| --- | --- |
| [CustomValueType](arkts-ime-customvaluetype-t.md) | Represents the extension information type. The specific type of the parameter depends on its functionality. |

