# @ohos.arkui.Prefetcher(Prefetching)

/*
 Copyright (c) 2024 Huawei Device Co., Ltd.
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


## Modules to Import

```TypeScript
import { IDataSourcePrefetching } from 'IDataSourcePrefetching';
import { IPrefetcher } from 'IPrefetcher';
import { BasicPrefetcher } from 'BasicPrefetcher';
```

## Summary

### Classes

| Name | Description |
| --- | --- |
| [BasicPrefetcher](arkts-arkui-arkui-prefetcher-basicprefetcher-c.md) | **BasicPrefetcher** is a fundamental implementation of **IPrefetcher**. It offers an intelligent data prefetching algorithm that decides the data items to prefetch based on real-time changes in the visible area on the screen and variations in the prefetch duration. It can also determine the prefetch requests to be canceled based on the user's scrolling actions. **BasicPrefetcher** objects do not support JSON serialization. |

### Interfaces

| Name | Description |
| --- | --- |
| [IDataSourcePrefetching](arkts-arkui-arkui-prefetcher-idatasourceprefetching-i.md) | Extends the IDataSource API to provide a data source that can be prefetched. |
| [IPrefetcher](arkts-arkui-arkui-prefetcher-iprefetcher-i.md) | Provides the prefetching capability. It works with **LazyForEach** to prefetch data items when users swipe through container components such as **List** and **Grid**, improving user browsing experience. |

