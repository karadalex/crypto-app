import * as React from 'react';
import { useQuery, gql } from '@apollo/client';
import { StyleSheet, Button } from 'react-native';
import { Text, View } from '../components/Themed';
import Container from '../components/Container';
import ScreenTitle from '../components/ScreenTitle'


const USER_QUERY = gql`
  query Users {
    user(user_Id: 1) {
      email,
      firstName,
      lastName
    }
  }
`;

export default function Account() {
  const { loading, error, data, refetch } = useQuery(USER_QUERY);

  return (
    <Container>
      <ScreenTitle>Account</ScreenTitle>
      {loading && <Text>Loading...</Text>}
      {error && <Text>Error :(</Text>}
      {data && (
        <React.Fragment>
          <Text>{JSON.stringify(data.user)}</Text>
          <Button
            onPress={() => refetch()}
            title="Refresh"
            accessibilityLabel="Refresh account details"
          />
        </React.Fragment>
      )}
    </Container>
  );
}
