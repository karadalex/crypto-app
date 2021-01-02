import React from 'react';
import { storiesOf } from '@storybook/react-native';
import Container from '../../../components/Container';
import ScreenTitle from '../../../components/ScreenTitle'
import { Text } from 'react-native';

storiesOf('Container', module)
  .add('with simple text', () => (
    <Container>
      <Text>Custom view using styled components</Text>
    </Container>
  ))
  .add('with screen title', () => (
    <Container>
      <ScreenTitle>ScreenTitle</ScreenTitle>
    </Container>
  ));
