# @ohos.pluginComponent(PluginComponentManager)

本模块供插件组件的使用方请求组件与数据，供提供方发送组件模板和数据。
 ###### 关于 external.json 文件
 **external.json**文件由开发者创建。该文件以键值对形式存储组件名称和模板路径。
 组件名称作为关键字，对应的模板路径作为值。
 **示例**
 ```json
 {
 "PluginProviderExample": "ets/pages/PluginProviderExample.js",
 "plugintemplate2": "ets/pages/plugintemplate2.js"
 }
 ```


## 导入模块

```TypeScript
import { pluginComponentManager, PluginComponentTemplate } from 'kits/@kit.ArkUI';
```

## 汇总

### 命名空间

| 名称 |
| --- |
| [pluginComponentManager(PluginComponentManager)](arkts-arkui-plugincomponentmanager-n.md) |

### 接口

| 名称 |
| --- |
| [PluginComponentTemplate(PluginComponentManager)](arkts-arkui-plugincomponent-plugincomponenttemplate-i.md) |
