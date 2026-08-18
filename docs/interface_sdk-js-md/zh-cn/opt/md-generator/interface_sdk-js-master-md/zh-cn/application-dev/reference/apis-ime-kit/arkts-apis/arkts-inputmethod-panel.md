# @ohos.inputMethod.Panel(输入法面板)

/*
 Copyright (c) 2023 Huawei Device Co., Ltd.
 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at
 http://www.apache.org/licenses/LICENSE-2.0
 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
 /
 **@ohos.inputMethod.Panel**模块提供输入法面板属性的数据定义，支持配置面板的类型和显示状态，适用于需要精细化控制输入法面板显示行为的场景。
 本模块是输入法框架的面板属性数据模块，定义了`PanelInfo`接口以及`PanelType`、`PanelFlag`两个枚举类型，用于描述输入法面板的类型（软键盘或状态栏）和显示状态（固定态、悬浮态、候选词态）。
 本模块提供输入法面板属性的配置能力。输入法应用可通过`PanelInfo`指定面板类型和状态类型，实现不同形态的面板展示——固定态软键盘（默认，固定在屏幕底部）、悬浮态软键盘（可自由拖动位置）、候选词态面板（独立窗口展示候选词，由开发
 者自行控制显隐）。
 当输入法应用需要创建和配置输入法面板时使用本模块。典型场景包括：输入法应用创建默认固定态软键盘面板、输入法应用创建悬浮态键盘以支持自由拖动、输入法应用创建候选词面板以展示输入候选。
 数据类型需与`@ohos.inputMethodEngine`模块的API组合使用——在`InputMethodAbility.createPanel()`创建面板时传入`PanelInfo`指定面板类型和状态。典型使用流程：构造
 PanelInfo → 通过createPanel传入 → 系统据此创建对应类型的面板。不同PanelFlag值对应不同的面板行为：固定态面板固定在屏幕底部、悬浮态面板可自由拖动、候选词态面板由开发者自行控制显隐。
 本模块定义了以下关键Interface和枚举类型：
| Interface/类型 |
|---|
| **PanelInfo** |
| **PanelType** |
| **PanelFlag** |
 本模块为纯数据定义模块，`PanelInfo`作为面板属性配置需与其他模块的API组合使用。典型组合为：在`@ohos.inputMethodEngine`模块中，通过
 `InputMethodAbility.createPanel()`创建面板时传入`PanelInfo`指定面板类型和状态。


## 导入模块

```TypeScript
```

## 汇总

### 接口

| 名称 |
| --- |
| [PanelInfo](arkts-ime-inputmethod-panel-panelinfo-i.md) |

### 枚举

| 名称 |
| --- |
| [PanelFlag](arkts-ime-inputmethod-panel-panelflag-e.md) |
| [PanelType](arkts-ime-inputmethod-panel-paneltype-e.md) |
