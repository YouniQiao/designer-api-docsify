# @ohos.InputMethodExtensionContext(InputMethodExtensionContext)

###### Usage
 Before using the **InputMethodExtensionContext** module, you must define a child class that inherits from
 **InputMethodExtensionAbility**.
 <br>
 <br>```ts
 <br>import { InputMethodExtensionAbility, InputMethodExtensionContext } from '@kit.IMEKit';
 <br>import { Want } from '@kit.AbilityKit';
 <br>class InputMethodExtAbility extends InputMethodExtensionAbility {
 <br>  onCreate(want: Want): void {
 <br>    console.info('onCreate, want:' + want.abilityName);
 <br>  }
 <br>}
 <br>```


## Modules to Import

```TypeScript
import { InputMethodExtensionContext } from '@kit.IMEKit';
```

## Summary

### Classes

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [InputMethodExtensionContext(InputMethodExtensionContext)](arkts-ime-inputmethodextensioncontext-c.md) |

<!--Del-->
### Classes(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [InputMethodExtensionContext(InputMethodExtensionContext)](arkts-ime-inputmethodextensioncontext-c-sys.md) |
<!--DelEnd-->
