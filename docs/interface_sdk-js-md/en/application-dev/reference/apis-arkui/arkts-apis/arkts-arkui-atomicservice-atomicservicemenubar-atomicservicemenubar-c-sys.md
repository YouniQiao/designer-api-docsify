# AtomicServiceMenuBar (System API)

Creates an **AtomicServiceMenuBar** object based on the context of the current atomic service. The object is used to control the display of the menu function capsule in the upper right corner.

**Since:** 23

<!--Device-unnamed-/* * Copyright (c) 2025 Huawei Device Co., Ltd. * Licensed under the Apache License, Version 2.0 (the "License"); * you may not use this file except in compliance with the License. * You may obtain a copy of the License at * *     http://www.apache.org/licenses/LICENSE-2.0 * * Unless required by applicable law or agreed to in writing, software * distributed under the License is distributed on an "AS IS" BASIS, * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. * See the License for the specific language governing permissions and * limitations under the License. */export declare class AtomicServiceMenuBar--><!--Device-unnamed-/* * Copyright (c) 2025 Huawei Device Co., Ltd. * Licensed under the Apache License, Version 2.0 (the "License"); * you may not use this file except in compliance with the License. * You may obtain a copy of the License at * *     http://www.apache.org/licenses/LICENSE-2.0 * * Unless required by applicable law or agreed to in writing, software * distributed under the License is distributed on an "AS IS" BASIS, * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. * See the License for the specific language governing permissions and * limitations under the License. */export declare class AtomicServiceMenuBar-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { AtomicServiceMenuBar } from '@kit.ArkUI';
```

## constructor

```TypeScript
constructor(uiContext: UIContext)
```

A constructor used to create an **AtomicServiceMenuBar** object.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-AtomicServiceMenuBar-constructor(uiContext: UIContext)--><!--Device-AtomicServiceMenuBar-constructor(uiContext: UIContext)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uiContext | [UIContext](../arkts-components/arkts-arkui-uicontext-t.md) | Yes | Context information of the current atomic service. |

## setVisible

```TypeScript
public setVisible(visible: boolean): void
```

Sets whether to display or hide the menu function capsule of the current atomic service.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-AtomicServiceMenuBar-public setVisible(visible: boolean): void--><!--Device-AtomicServiceMenuBar-public setVisible(visible: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| visible | boolean | Yes | Expected status of the menu function capsule. true: The menu function capsule is displayed. false: The menu function capsule is hidden. |

