# @ohos.pluginComponent(PluginComponentManager)

The **PluginComponentManager** module provides APIs for the **PluginComponent** user to request components and data
 and send component templates and data.
 ###### About the external.json File
 The **external.json** file is created by developers. It stores component names and template paths in key-value pairs.
 The component name is used as the keyword, and the corresponding template path is used as the value.
 **Example**
 ```json
 {
 "PluginProviderExample": "ets/pages/PluginProviderExample.js",
 "plugintemplate2": "ets/pages/plugintemplate2.js"
 }
 ```


## Modules to Import

```TypeScript
import { PluginComponentTemplate } from '@kit.ArkUI';
```

## Summary

### Namespaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [pluginComponentManager](arkts-arkui-plugincomponentmanager-n.md) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [PluginComponentTemplate](arkts-arkui-plugincomponent-plugincomponenttemplate-i.md) |
