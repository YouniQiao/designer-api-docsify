# @ohos.atomicservice.NavPushPathHelper(Defines provides a push method for the target page in the routing table.)

###### Child Components
 Not supported
 ###### Attributes
 The [universal attributes](../../apis-arkui/arkts-components/arkts-arkui-common-attribute.md) are not supported.
 ###### Events
 The [universal events](../../apis-arkui/arkts-components/arkts-arkui-common-attribute.md) are not supported.


## Modules to Import

```TypeScript
import { NavPushPathHelper } from 'kits/@kit.ArkUI';
```

## Summary

### Classes

| Name | Description |
| --- | --- |
| [NavPushPathHelper](arkts-arkui-atomicservice-navpushpathhelper-navpushpathhelper-c.md) | On the initial launch, the atomic service only downloads and installs the main package and its dependencies.Therefore, if the [NavDestination](../../apis-arkui/arkts-components/arkts-arkui-nav_destination-i) resides in a different HSP subpackage that is not a dependency of the main package, you'll need to use **NavPushPathHelper** to download and install the corresponding HSP subpackage first. After that, push the specified **NavDestination** page information onto the stack. This way, you enable [Navigation](../../apis-arkui/arkts-components/arkts-arkui-navigation-i) to support dynamic loading of the HSP subpackage before the navigation occurs. |

