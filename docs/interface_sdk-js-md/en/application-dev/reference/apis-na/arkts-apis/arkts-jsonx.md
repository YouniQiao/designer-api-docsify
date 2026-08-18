# Jsonx

/*
 Copyright (c) 2026 Huawei Device Co., Ltd.
 Licensed under the Apache License, Version 2.0 (the "License"),
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at
 http://www.apache.org/licenses/LICENSE-2.0
 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
 /


**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export namespace jsonx--><!--Device-unnamed-export namespace jsonx-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
```

## Summary

### Classes

| Name | Description |
| --- | --- |
| [JsonElement](arkts-na-jsonx-jsonelement-c.md) | Core class representing a JSON element that can hold any valid JSON value. Provides type-safe access to JSON values with both strict and lenient APIs. The class maintains an invariant that only one type of value can be set at a time. Attempting to set multiple values will result in a JsonTypeError. |
| [JsonError](arkts-na-jsonx-jsonerror-c.md) | Base error class for JSON-related errors. Thrown when general JSON parsing or manipulation errors occur. |
| [JsonTypeError](arkts-na-jsonx-jsontypeerror-c.md) | Error thrown when attempting to access a JSON element with an incompatible type. For example, trying to get a string value from a number element. |

### Interfaces

| Name | Description |
| --- | --- |
| [JsonElementDeserializable](arkts-na-jsonx-jsonelementdeserializable-i.md) | Interface for types that can be serialized to JSON. Classes implementing this interface can be converted to a JsonElement. |
| [JsonElementSerializable](arkts-na-jsonx-jsonelementserializable-i.md) | Interface for types that can be deserialized from JSON. Classes implementing this interface can be converted from a JsonElement. |
| [ParseOptions](arkts-na-jsonx-parseoptions-i.md) | ParseOptions for JSON.parse to pass BigIntMode. |

### Enums

| Name | Description |
| --- | --- |
| [BigIntMode](arkts-na-jsonx-bigintmode-e.md) | Enumeration of BigIntMode. |
| [JsonType](arkts-na-jsonx-jsontype-e.md) | Enumeration of possible JSON value types. Used to identify the type of a JsonElement at runtime. |

