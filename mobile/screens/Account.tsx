import * as React from 'react';
import { useQuery, gql } from '@apollo/client';
import { StyleSheet, Button } from 'react-native';
import { Text, View } from '../components/Themed';


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
    <View style={styles.container}>
      <Text style={styles.title}>Account</Text>
      {loading && <Text>Loading...</Text>}
      {error && <Text>Error :(</Text>}
      {data && (
        <React.Fragment>
          <Text>{JSON.stringify(data.user)}</Text>
          <Button
            onPress={() => refetch()}
            title="Learn More"
            accessibilityLabel="Learn more about this purple button"
          />
        </React.Fragment>
      )}
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    marginHorizontal: 20,
    marginTop: 50,
    backgroundColor: "transparent"
  },
  title: {
    fontSize: 35,
    fontWeight: 'bold',
  },
  separator: {
    marginVertical: 30,
    height: 1,
    width: '80%',
  },
});
