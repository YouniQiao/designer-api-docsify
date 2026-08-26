# ComponentContent

## Summary

### Classes

| Name | Description |
| --- | --- |
| [ComponentContent](arkts-arkui-componentcontent-c.md) | You can create an entity encapsulation component in either of the following ways: You can select either of the following methods during development:  **ComponentContent** represents an entity encapsulation of component content, which can be created and transmitted outside of UI components. It allows you to encapsulate and decouple dialog box components. Its underlying implementation uses BuilderNode. For details, see BuilderNode.  **ReactiveComponentContent** represents an entity encapsulation of component content, which can be created and transmitted outside of UI components. It allows you to encapsulate and decouple dialog box components. Its underlying implementation uses **ReactiveBuilderNode**. For details, see [ReactiveBuilderNode](arkts-arkui-buildernode-reactivebuildernode-c.md). |
| [ReactiveComponentContent](arkts-arkui-componentcontent-reactivecomponentcontent-c.md) | ReactiveComponentContent is inherited from [Content](../../../reference/apis-arkui/js-apis-arkui-Content.md#content-1) and is a container component used to dynamically bear and reuse UI content. It uses the @Builder function to build the UI and uses [ReactiveBuilderNode](arkts-arkui-buildernode-reactivebuildernode-c.md) to generate and manage the component tree. The core value of this component is to provide complete lifecycle management for dynamic content so that it can be integrated into the ArkUI component reuse system. This component is especially suitable for scenarios that require high- performance rendering, such as number lists. |
