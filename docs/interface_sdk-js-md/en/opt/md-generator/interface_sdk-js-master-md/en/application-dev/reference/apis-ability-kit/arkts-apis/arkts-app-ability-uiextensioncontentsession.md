# @ohos.app.ability.UIExtensionContentSession

UIExtensionContentSession is the UI operation class for the
 [UIExtensionAbility](arkts-ability-app-ability-uiextensionability-uiextensionability-c.md). It provides control over page
 loading and allows configuration of the window privacy mode of the host application (application that starts the
 UIExtensionAbility). When the host application starts a specific UIExtensionAbility, the system creates a
 UIExtensionContentSession object and passes it back via the
 [onSessionCreate](arkts-ability-app-ability-uiextensionability-uiextensionability-c.md#onsessioncreate) callback. Each
 UIExtensionAbility corresponds to one UIExtensionContentSession object, and these objects operate independently
 without interfering with each other.


## Modules to Import

```TypeScript
import { UIExtensionContentSession } from 'kits/@kit.AbilityKit';
```

## Summary

### Classes

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [UIExtensionContentSession](arkts-ability-app-ability-uiextensioncontentsession-uiextensioncontentsession-c.md) |

<!--Del-->
### Classes（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [UIExtensionContentSession](arkts-ability-app-ability-uiextensioncontentsession-uiextensioncontentsession-c-sys.md) |
<!--DelEnd-->
